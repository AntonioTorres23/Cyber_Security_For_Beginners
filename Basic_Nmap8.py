import nmap
import platform
import os
import datetime
import json
from multiprocessing import Pool
import shutil


def file_mov(fi, directory):

    if platform.system() == 'Windows' or 'windows':
        dest = f"{os.getcwd()}\\{directory}\\{fi}"
        shutil.move(fi, dest)

    elif platform.system() == 'Linux' or 'linux' or 'Darwin' or 'darwin':
        dest = f"{os.getcwd()}/{directory}/{fi}"
        shutil.move(fi, dest)


def get_dir():

    fol = os.listdir(os.getcwd())

    for fi in fol:
        match fi:
            case fi if ".log" in fi:
                ls_fi = [fi]
                for x in ls_fi:
                    file_mov(x, "Honey_Pot_Logs")
            case fi if ".json" in fi:
                if platform.system() == "Windows" or "windows":
                    ls_fi = [fi]
                    for x in ls_fi:
                        file_mov(x, "Nmap_JSONs")
            case fi if ".pcap" in fi:
                ls_fi = [fi]
                for x in ls_fi:
                    file_mov(x, "Pyshark_PCAPs")
            case fi if "Output_From_Ping_Sweep" in fi:
                ls_fi = [fi]
                for x in ls_fi:
                    file_mov(x, "Ping_Sweeps")


netmap = nmap.PortScanner()


def the_scan(addr, what_ports, options):

    netmap.scan(hosts=addr, ports=what_ports, arguments=options)

    for host in netmap.all_hosts():

        the_hosts = netmap[host]

        if "255" in host:
            break

        print(the_hosts)

        print(f"Hosts: {host} ")

        the_state = f"State: {netmap[host].state()}"

        print(f"State: {netmap[host].state()}")

        the_hostname = f"Name: {netmap[host].hostname()}"

        print(f"Name: {netmap[host].hostname()}")

        if '-O' in options:

            the_os = netmap[host]['osmatch']

            print(netmap[host]['osmatch'])
        else:

            the_os = [""]

        for protocol in netmap[host].all_protocols():

            the_protocol = f"Protocol {protocol}"

            print(f"Protocol {protocol}")

            list_ports = netmap[host][protocol].keys()

            sorted_stuff = sorted(list_ports)

            for port in list_ports:
                print(f"Ports: {port}")

            scan_res = the_hosts, sorted_stuff, the_protocol, the_hostname, the_state, the_os

            return scan_res


def main():
    the_scan(addr, what_ports, options)


if __name__ == '__main__':
    comp_os = platform.system()

    if comp_os == "Windows" or comp_os == "windows":

        os.system("route PRINT")
    elif comp_os == "Linux" or comp_os == "linux":

        os.system("route")

    elif comp_os == "Darwin" or comp_os == "darwin":

        os.system("route")

    else:
        print("Sorry Unknown OS")

    addr = input("Enter the IP address or Route Address you want to begin scanning: ")

    what_ports = input("Example Formatting: 22-443\nWhat ports do you want to scan?: ")

    options = input("Examples -sS,-O or -F:\n Enter your Arguments: ")

    pool = Pool(processes=60)

    res = pool.apply_async(the_scan, args=(addr, what_ports, options))

    pool.close()

    pool.join()

    results = res.get()

    now = datetime.datetime.now()

    str_dt = now.strftime("%y-%m-%d_%H-%M-%S")

    new_fi = open(f"nmap_scan_{str_dt}.json", "a")

    new_fi.write(json.dumps(results, indent=0))

    input("Press Any Key to Exit\n")

    new_fi.close()

    start_t = datetime.datetime.now()
    end_t = start_t + datetime.timedelta(seconds=3)
    while end_t > datetime.datetime.now():
        print("Syncing, Please Wait...")
        get_dir()
