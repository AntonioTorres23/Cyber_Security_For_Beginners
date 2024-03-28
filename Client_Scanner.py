import platform
import os
from scapy.layers.l2 import ARP, Ether, srp


def arp_func(dest_ip):
    arp = ARP(pdst=dest_ip)

    ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")

    pack = ethernet / arp

    res = srp(pack, timeout=3, verbose=0)[0]

    clis = []

    for sen, rec in res:
        clis.append({'ip': rec.psrc, 'mac': rec.hwsrc})

    print("Devices on the network with corresponding MAC Addresses")

    for cli in clis:
        print(f"{cli['ip']} {cli['mac']}")


def main():
    comp_os = platform.system()

    if comp_os == "Windows" or comp_os == "windows":
        os.system("ipconfig")
    elif comp_os == "Linux" or comp_os == "linux":
        os.system("ifconfig")
    elif comp_os == "Darwin" or comp_os == "darwin":
        os.system("ifconfig")
    else:
        print("Sorry Unknown OS")
    dest_ip = input("Enter the subnet you want to sweep: ")
    arp_func(dest_ip)


if __name__ == '__main__':
    main()