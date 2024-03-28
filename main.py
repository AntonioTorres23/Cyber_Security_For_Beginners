import datetime
import os
import platform
import shutil
import threading
import art
from termcolor import colored
import Banner_Grabber
import Client_Scanner
import Packet_Sniffer3
import Ping


def file_mov_win(fi, directory):
    if platform.system():
        dest = f"{os.getcwd()}\\{directory}\\{fi}"
        shutil.move(fi, dest)


def file_mov_uni(fi, directory):
    if platform.system() == 'Linux' or 'linux' or 'Darwin' or 'darwin':
        dest = f"{os.getcwd()}/{directory}/{fi}"
        shutil.move(fi, dest)


def get_dir():
    comp_os = platform.system()

    match comp_os:

        case "Windows":

            dirs = [f"{os.getcwd()}\\Honey_Pot_Logs", f"{os.getcwd()}\\Nmap_JSONs", f"{os.getcwd()}\\Pyshark_PCAPs",
                    f"{os.getcwd()}\\Ping_Sweeps"]
            for x in dirs:
                if not os.path.exists(x):
                    os.mkdir(x)
        case "windows":
            dirs = [f"{os.getcwd()}\\Honey_Pot_Logs", f"{os.getcwd()}\\Nmap_JSONs", f"{os.getcwd()}\\Pyshark_PCAPs",
                    f"{os.getcwd()}\\Ping_Sweeps"]
            for x in dirs:
                if not os.path.exists(x):
                    os.mkdir(x)

        case "Linux":

            dirs = [f"{os.getcwd()}/Honey_Pot_Logs", f"{os.getcwd()}/Nmap_JSONs", f"{os.getcwd()}/Pyshark_PCAPs",
                    f"{os.getcwd()}/Ping_Sweeps"]

            for x in dirs:
                if not os.path.exists(x):
                    os.mkdir(x)
        case "linux":
            dirs = [f"{os.getcwd()}/Honey_Pot_Logs", f"{os.getcwd()}/Nmap_JSONs", f"{os.getcwd()}/Pyshark_PCAPs",
                    f"{os.getcwd()}/Ping_Sweeps"]

            for x in dirs:
                if not os.path.exists(x):
                    os.mkdir(x)
        case "Darwin":
            dirs = [f"{os.getcwd()}/Honey_Pot_Logs", f"{os.getcwd()}/Nmap_JSONs", f"{os.getcwd()}/Pyshark_PCAPs",
                    f"{os.getcwd()}/Ping_Sweeps"]

            for x in dirs:
                if not os.path.exists(x):
                    os.mkdir(x)
        case "darwin":
            dirs = [f"{os.getcwd()}/Honey_Pot_Logs", f"{os.getcwd()}/Nmap_JSONs", f"{os.getcwd()}/Pyshark_PCAPs",
                    f"{os.getcwd()}/Ping_Sweeps"]

            for x in dirs:
                if not os.path.exists(x):
                    os.mkdir(x)

    fol = os.listdir(os.getcwd())
    match comp_os:

        case "Windows":
            for fi in fol:
                if platform.system() == "Windows" or "windows":
                    match fi:
                        case fi if ".log" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_win(x, "Honey_Pot_Logs")
                        case fi if ".json" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_win(x, "Nmap_JSONs")
                        case fi if ".pcap" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_win(x, "Pyshark_PCAPs")
                        case fi if "Output_From_Ping_Sweep" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_win(x, "Ping_Sweeps")
        case "Linux":
            for fi in fol:
                if platform.system() == "Linux" or "linux" or "Darwin" or "darwin":
                    match fi:
                        case fi if ".log" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Honey_Pot_Logs")
                        case fi if ".json" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Nmap_JSONs")
                        case fi if ".pcap" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Pyshark_PCAPs")
                        case fi if "Output_From_Ping_Sweep" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Ping_Sweeps")
        case "linux":
            for fi in fol:
                if platform.system() == "Linux" or "linux" or "Darwin" or "darwin":
                    match fi:
                        case fi if ".log" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Honey_Pot_Logs")
                        case fi if ".json" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Nmap_JSONs")
                        case fi if ".pcap" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Pyshark_PCAPs")
                        case fi if "Output_From_Ping_Sweep" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Ping_Sweeps")
        case "Darwin":
            for fi in fol:
                if platform.system() == "Linux" or "linux" or "Darwin" or "darwin":
                    match fi:
                        case fi if ".log" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Honey_Pot_Logs")
                        case fi if ".json" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Nmap_JSONs")
                        case fi if ".pcap" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Pyshark_PCAPs")
                        case fi if "Output_From_Ping_Sweep" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Ping_Sweeps")
        case "darwin":
            for fi in fol:
                if platform.system() == "Linux" or "linux" or "Darwin" or "darwin":
                    match fi:
                        case fi if ".log" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Honey_Pot_Logs")
                        case fi if ".json" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Nmap_JSONs")
                        case fi if ".pcap" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Pyshark_PCAPs")
                        case fi if "Output_From_Ping_Sweep" in fi:
                            ls_fi = [fi]
                            for x in ls_fi:
                                file_mov_uni(x, "Ping_Sweeps")


def cls():
    comp_os = platform.system()

    if comp_os == "Windows" or comp_os == "windows":
        os.system('cls')
    elif comp_os == 'Linux' or comp_os == "linux":
        os.system('clear')
    elif comp_os == 'darwin' or comp_os == 'Darwin':
        os.system('clear')


def ga(a):
    while True:
        go_again = input("Would you like to go again? (y/n)\nEnter Here: ")
        if go_again == 'y' or go_again == 'Y':
            cls()
            a()
            break
        elif go_again == 'N' or go_again == 'n':
            cls()
            main()
            break


def what_os_win(py_fi):
    opsys = platform.system()
    if opsys == 'Windows' or 'windows':
        os.startfile(py_fi + ".py")


def what_os_uni(py_fi):
    opsys = platform.system()
    if opsys == 'Linux' or 'linux' or 'Darwin' or 'darwin':
        os.system(f"python3 {os.getcwd()}/{py_fi}.py")


def main():
    comp_os = platform.system()

    t = threading.Thread(target=get_dir)
    t.start()

    while True:

        inp = input("1): Network Ping Sweep\n2): Banner Grabber\n3): Nmap Scanner\n4): Client "
                    "Scanner\n"
                    "5): Packet Sniffer\n6): Honey Pot\nEnter c to clear screen.\nPress s to sync files to folders\n"
                    "Or, Enter d for documentation.\n"
                    "Press q to quit.\nEnter"
                    " Here: ")

        match inp:
            case "1":
                print("Ok, Loading Ping Sweep")
                cls()
                Ping.main()
                while True:
                    ga(Ping.main)

            case "2":
                print("Ok, Loading Banner Grabber")
                cls()
                Banner_Grabber.main()
                while True:
                    ga(Banner_Grabber.main)

            case "3":
                print("Ok, Loading Nmap Scanner")
                match comp_os:
                    case "Windows":
                        cls()
                        what_os_win("Basic_Nmap8")
                    case "windows":
                        cls()
                        what_os_win("Basic_Nmap8")
                    case "Linux":
                        cls()
                        what_os_uni("Basic_Nmap8")
                    case "linux":
                        cls()
                        what_os_uni("Basic_Nmap8")
                    case "Darwin":
                        cls()
                        what_os_uni("Basic_Nmap8")
                    case "darwin":
                        cls()
                        what_os_uni("Basic_Nmap8")

            case "4":
                print("Ok, Loading Client Scanner")
                cls()
                Client_Scanner.main()
                while True:
                    ga(Client_Scanner.main)

            case "5":
                cls()
                print("Ok, Loading Packet Sniffer")
                Packet_Sniffer3.main()
                while True:
                    ga(Packet_Sniffer3.main)
            case "6":
                print("Ok, Loading Honey Pot")
                match comp_os:
                    case "Windows":
                        cls()
                        what_os_win("Honey_Pot2")
                    case "windows":
                        cls()
                        what_os_win("Honey_Pot2")
                    case "Linux":
                        cls()
                        what_os_uni("Honey_Pot2")
                    case "linux":
                        cls()
                        what_os_uni("Honey_Pot2")
                    case "Darwin":
                        cls()
                        what_os_uni("Honey_Pot2")
                    case "darwin":
                        cls()
                        what_os_uni("Honey_Pot2")
            case "c":
                cls()
            case "C":
                cls()
            case "d":
                cls()
                match comp_os:
                    case "Windows":
                        cls()
                        what_os_win("Docs")
                    case "windows":
                        cls()
                        what_os_win("Docs")
                    case "Linux":
                        cls()
                        what_os_uni("Docs")
                    case "linux":
                        cls()
                        what_os_uni("Docs")
                    case "Darwin":
                        cls()
                        what_os_uni("Docs")
                    case "darwin":
                        cls()
                        what_os_uni("Docs")
            case "D":
                cls()
                match comp_os:
                    case "Windows":
                        cls()
                        what_os_win("Docs")
                    case "windows":
                        cls()
                        what_os_win("Docs")
                    case "Linux":
                        cls()
                        what_os_uni("Docs")
                    case "linux":
                        cls()
                        what_os_uni("Docs")
                    case "Darwin":
                        cls()
                        what_os_uni("Docs")
                    case "darwin":
                        cls()
                        what_os_uni("Docs")
            case "q":
                cls()
                start_t = datetime.datetime.now()
                end_t = start_t + datetime.timedelta(seconds=3)
                while end_t > datetime.datetime.now():
                    print("Syncing, Please Wait...")
                    get_dir()
                exit()
            case "Q":
                cls()
                start_t = datetime.datetime.now()
                end_t = start_t + datetime.timedelta(seconds=3)
                while end_t > datetime.datetime.now():
                    print("Syncing, Please Wait...")
                    get_dir()
                exit()
            case "S":
                cls()
                start_t = datetime.datetime.now()
                end_t = start_t + datetime.timedelta(seconds=3)
                while end_t > datetime.datetime.now():
                    print("Syncing, Please Wait...")
                    get_dir()
                cls()
            case "s":

                cls()
                start_t = datetime.datetime.now()
                end_t = start_t + datetime.timedelta(seconds=3)
                while end_t > datetime.datetime.now():
                    print("Syncing, Please Wait...")
                    get_dir()
                cls()
            case _:
                cls()
                print("Sorry I don't know that answer.\nPlease Try Again.")


print(colored(art.text2art(font="Poison", text="Welcome to"), color="green"))
print(colored(art.text2art(font="Poison", text="Cyber Security"), color="green"))
print(colored(art.text2art(font="Poison", text=" for"), color="green"))
print(colored(art.text2art(font="Poison", text="Beginners"), color="green"))
print(colored(art.text2art(font="graffiti", text="By: "), color="green"))
print(colored(art.text2art(font="graffiti", text="Antonio"), color="green"))
print(colored(art.text2art(font="graffiti", text="Torres "), color="green"))
input(colored("Press Any Key to Continue", color="green"))

cls()

print("Now that we are through with introductions,\nWhat would you like to do?\n")

if __name__ == '__main__':
    main()
