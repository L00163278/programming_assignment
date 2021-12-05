"""
# -----------------------------
# File : L00163278_Q4_File_2.py
# Created :  27/11/2021 21:22
# Author : Rohit Mishra
# Version : v1.0.0
# Licensing : (C) 2021 Rohit Mishra, LYIT
#              Available under GNU Public License (GPL)
# Description : Display which ports are open in the Ubuntu VM
# -----------------------------
"""

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    """
        Port Scan method of connection
        Connecting to the ports
        Parameters:
        none
        Returns:
        none
    """

    # Clear the screen  #use clear if running in  *nix
    subprocess.call("cls", shell=True)

    # Ask for input
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors

    try:
        # try 1, 1025 if you have time
        for port in range(1, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                name = ''  # initial value.
                if port == 80:
                    name = 'HTTP'
                elif port == 22:
                    name = 'SSH'
                print("Port {}: 	 Open     {}".format(port, name))
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)


if __name__ == "__main__":
    """
        Main method of generating port details
        Display which ports are open
        Parameters:
        none
        Returns:
        none
        """
    port_scan()
