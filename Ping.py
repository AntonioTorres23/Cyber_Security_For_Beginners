import ipaddress
from ping3 import ping
import datetime
import os
import platform
from termcolor import colored


def sweep(sn):
    net = ipaddress.ip_network(sn, strict=False)
    other_now = datetime.datetime.now()
    str_dt = other_now.strftime("%y-%m-%d_%H-%M-%S")
    with open(f"Output_From_Ping_Sweep_{str_dt}.txt", "a") as file:
        for raw_ip in net.hosts():
            conv_ip = str(raw_ip)
            try:
                resp_tim = ping(conv_ip, timeout=4)
                if resp_tim is not None:
                    now = datetime.datetime.now()
                    reply_back = colored(f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {conv_ip} is up", "green")
                    no_col_reply_back = f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {conv_ip} is up"
                    if "255" in conv_ip:
                        conv_ip = conv_ip
                        try:
                            ping(conv_ip, timeout=4)
                            if resp_tim is not None:

                                other_rep = colored(f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {conv_ip} is up", "green")
                                no_col_other_rep = f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {conv_ip} is up"
                            else:

                                other_rep = colored(f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {conv_ip} is not up", "red")
                                no_col_other_rep = f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {conv_ip} is not up"
                        except Exception:
                            f"Could not ping {conv_ip}"
                        print(other_rep)
                        file.writelines(no_col_other_rep)
                        return conv_ip
                else:
                    now = datetime.datetime.now()
                    reply_back = colored(f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {conv_ip} not up", "red")
                    no_col_reply_back = f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {conv_ip} not up"
            except Exception:
                f"Could not ping {conv_ip}"
            print(reply_back)
            file.writelines(no_col_reply_back + '\n')


def main():
    comp_os = platform.system()

    if comp_os == "Windows" or comp_os == "windows":
        os.system("route PRINT")
        os.system("ipconfig")
    elif comp_os == "Linux" or comp_os == "linux":
        os.system("route")
        os.system("ifconfig")
    elif comp_os == "Darwin" or comp_os == "darwin":
        os.system("route")
        os.system("ifconfig")
    else:
        print("Sorry Unknown OS")

    sn = input("Enter the subnet you want to sweep: ")
    try:

        sweep(sn)
    except Exception:
        print("Something went wrong. Please try again.")


if __name__ == '__main__':
    main()
