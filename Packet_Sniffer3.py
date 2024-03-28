import datetime
import os
import platform
import pyshark


def main():
    comp_os = platform.system()

    if comp_os == "Windows" or comp_os == "windows":
        os.system("ipconfig")
    elif comp_os == "Linux" or comp_os == "linux":
        os.system("ip link")
    elif comp_os == "Darwin" or comp_os == "darwin":
        os.system("ip link")
    else:
        print("Sorry Unknown OS")

    while True:

        interface_inp = input("Enter what interface you want to scan: ")

        sav_2_file = input("Would you like to save to a file?\nEnter y/n: ")

        if sav_2_file == 'y' or sav_2_file == 'Y':
            now = datetime.datetime.now()
            str_dt = now.strftime("%y-%m-%d_%H-%M-%S")
            capture = pyshark.LiveCapture(output_file=f"pyshark_sniff_{str_dt}.pcap", interface=interface_inp)
            break
        elif sav_2_file == 'n' or sav_2_file == 'N':
            print("Ok Just a Scan Then.\n")
            capture = pyshark.LiveCapture(interface=interface_inp)
            break
        else:
            print("Invalid Answer. Please Try Again.")

    time_out = int(input("How long would you like to sniff before timing out?\nEnter Here:  "))

    sniff_for = int(input("How long would you like to sniff your network interface for? \nEnter Here: "))

    capture.sniff(timeout=time_out)

    print(capture)

    def sniff(capture):
        for pac_cap in capture.sniff_continuously(packet_count=sniff_for):
            print(pac_cap)

    sniff(capture)
