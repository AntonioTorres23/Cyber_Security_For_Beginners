import socket
import threading
import paramiko
import logging
import datetime
import sys
import art

now = datetime.datetime.now()

str_dt = now.strftime("%y-%m-%d_%H-%M-%S")

logger = logging.getLogger("")

logger.setLevel(logging.INFO)

file_hand = logging.FileHandler(f"Honey_Pot_Logs_{str_dt}.log")

stream_hand = logging.StreamHandler(sys.stdout)

forma = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_hand.setFormatter(forma)

stream_hand.setFormatter(forma)

logger.addHandler(file_hand)
logger.addHandler(stream_hand)


class SSH_SERVER(paramiko.ServerInterface):

    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        print(f"{username}:{password}")
        logger.info((username, password))
        return paramiko.common.AUTH_SUCCESSFUL

    def check_auth_publickey(self, username, key):
        logger.info((username, key))
        return paramiko.common.AUTH_FAILED

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            logger.info((kind, chanid))
            return paramiko.common.OPEN_SUCCEEDED
        return paramiko.common.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def get_allowed_auths(self, username):
        logger.info(username)
        return 'password'

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(
            self, channel, term, width, height, pixelwidth, pixelheight, modes
    ):
        return True


def handle_command(cmd, chan):
    resp = ""
    if cmd == "pwd":
        chan.send("PATH\r----\rC:\\Users\\Server_2\r" + "\r" + "\n")
        return
    elif cmd == "dir":
        send_text('dir.txt', chan)

        chan.send("\r\n")
        return

    elif cmd == "whoami":
        chan.send("desktop\\Server_2" + "\r" + "\n")
        return
    elif cmd.startswith("cd"):
        chan.send("I see what you are trying to do.\r\nLeave." + "\r" + "\n")
        return
    chan.send(resp + "\r\n")


def send_text(name, chan):
    with open(file=name) as txt:
        chan.send(b"\r")
        for x in enumerate(txt):
            chan.send(x[1] + "\r")

    chan.send("\r\n")


def handle_connection(client, key, client_ip):
    tran = paramiko.Transport(client)
    tran.add_server_key(key)
    ssh = SSH_SERVER()
    tran.start_server(server=ssh)
    chan = tran.accept(20)
    ssh.event.wait(10)
    try:
        chan.send(b"Server_2\r")

        terminal = True
        while terminal:
            chan.send(b"PS C:\\Users\\Server_2> ")
            cmd = ""
            while not cmd.endswith("\r"):
                tran = chan.recv(1024)
                chan.send(tran)
                cmd += tran.decode("utf-8")
            chan.send(b"\r\n")
            cmd = cmd.rstrip()
            logger.warning((client_ip, cmd))

            if cmd == "exit":
                terminal = False
            else:
                handle_command(cmd, chan)

    except:
        print("Error")


def main():
    print(art.text2art(font="graffiti", text="Honeypot"))
    print(art.text2art(font="graffiti", text="2.0"))
    serv_ip = input("Enter The IP that you would like the Honey Pot To Run On\nEnter Here: ")
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_sock.bind((serv_ip, 22))
    serv_sock.listen(100)

    serv_key = paramiko.RSAKey.generate(2048)
    a = paramiko.client.SSHClient()
    logging.warning(a)
    while True:
        client, client_ip = serv_sock.accept()
        logging.warning(f"Connection Attempt From: {client_ip}")

        th = threading.Thread(target=handle_connection, args=(client, serv_key, client_ip))
        th.start()


if __name__ == '__main__':
    main()
