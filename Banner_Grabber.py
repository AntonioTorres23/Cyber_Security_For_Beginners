import socket


def ban(ipadd, port_num):
    sock = socket.socket()
    try:
        sock.connect((ipadd, int(port_num)))
        print(sock.recv(1024))
    except:
        print("Unable to Connect to IP or Port\nPlease Check Your IP, Port, Or Network/Firewall Policies.")


def main():
    ipadd = input("Enter an IP: ")

    port_num = str(input("Enter a Port: "))
    ban(ipadd, port_num)


if __name__ == '__main__':
    print("Welcome to the Banner_Grabber Py Script")
    main()
    while True:
        go_again = input("Would you like to go again?\ny/n:")
        if go_again == 'y' or go_again == 'Y':
            print("Ok")
            main()
        elif go_again == "n" or go_again == "N":
            print("Goodbye")
            break
        else:
            print("Invalid Answer.\nPlease go again.")
