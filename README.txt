Welcome to Cybersecurity for Beginner's Documentation!

Some background on this project:

    - This project is my capstone for my final year in college.
    - It is a combination of multiple tools used by most Cybersecurity Professionals to assess and
      gather info on a network.
    - This project allows beginners to have these tools in an easy-to-use format.
    - This project also gives individuals an introduction to python and how powerful its
      standard/extended libraries are.

Some info on each script:

    -Main:
        - Where all the scripts are tied into one easy to use interface.
        - Uses switch case to clean and simplify multiple options rather than just if else statements.
        - Uses functions to take user input like go again or other QoL features like clearing the screen.
    -Ping:
        - A script that takes a subnet and sweeps through all 255 addresses.
        - Uses ipaddresses library to sweep subnet.
        - Uses try statement to prevent syntax errors from canceling the sweep loop.
    -Banner Grabber:
        - A script that allows you to scan a port and grab banner tags from it.
        - Allows you to get information on a system and what kind of software it is running for certain utilities.
        - Handles syntax errors with the except built-in.
    -Basic Nmap 6:
        - 6th iteration of this script I began working on in late January early February 2024.
        - Uses the official nmap library to preform port scans on a singular address or whole subnet.
        - Exports data into a JSON file for easier data sorting.
        - Uses multiprocessing to make the scan run faster.
    -Client Scanner:
        - Works with layer 2 and layer 3 client identifiers such as Mac Addresses and Ip Addresses to get an overall
          better view of the devices on a network.
        - Mac addresses are permanent on a device, so it makes them easier to identify.
        - Uses scapy, a library used for security scripts.
    -Packet Sniffer:
        - A way to sniff both wireless and wired packets.
        - As well as a way to save those scans to a file or look at the data as it is being gathered in real time.
        - Uses the pyshark library to preform sniffing and pcap saving functions.
    -Honey Pot 2:
        - A script that simulates an ssh Windows client when it is actually logging info such as their IP and
          SSL connections.
        - Uses Classes imported from Paramiko to Establish the SSH connection.
        - Paramiko is a library used for SSH connections with python.
        - Can be deployed on a server inside or outside the network.
        - Will always accept any password to trick users into thinking it has no password, or they guessed it right.
        - It grabs everything from what ssh software they used to connect to the port and ipaddresses they established
          a connection from.
        - Logs and Default Outputs to Shell are there for data analysis either in realtime or saved for a later date.
    -Docs:
        - The file you are viewing now.
        - Provides insight into the project and some background info on each script.

Special Thanks:
    - I would like to give a special thanks to securehoney.net, sudo Security on YouTube, nmap, cheeseandcereal on
      GitHub, tutorialspoint.com, w3schools.com, medium.com, Violent Python, Black Hat Python, the official python.org
      docs, scapy, paramiko, wireshark, and everyone on stackoverflow and GitHub. This project wouldn't be possible
      without these talented people.
Links:
    - https://github.com/cheeseandcereal/fake-ssh/blob/master/README.md

    - https://www.youtube.com/watch?v=OtEaIvIUipA

    - https://securehoney.net/blog/how-to-build-an-ssh-honeypot-in-python-and-docker-part-1.html

All Users:

    This project uses switch statements which is only compatible with versions of python 3.10 and above. I would
    recommend anything between 3.10 and 3.11 since 3.12 as of right now is having some issues with pip.

Linux Users:

    This project needs to be run in superuser to access all the programs. You can run sudo -E python3 main.py to do so.

A Warning for Users:

    THIS PROJECT IS INTENDED FOR WHITE HAT AND EDUCATIONAL PURPOSES ONLY. I AM NOT RESPONSIBLE FOR ANY WORK, LEGAL, OR
    ISP ISSUES THAT MAY ARISE WHEN USING THIS SOFTWARE.


