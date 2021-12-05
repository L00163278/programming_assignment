"""
# -----------------------------
# File : L00163278_Q3_File_1.py
# Created :  27/11/2021 20:25
# Author : Rohit Mishra
# Version : v1.0.0
# Licensing : (C) 2021 Rohit Mishra, LYIT
#              Available under GNU Public License (GPL)
# Description : Connection test to a VM using SSH port
# -----------------------------
"""

import paramiko
import time
import re


# Open SSH connection to the device
# first install ssh-server on the VM
#           sudo apt install openssh-server openssh-client
#
def ssh_connection(ip):
    """

            SSH method of application
            Connection test to a VM using SSH port
            Parameters:
             ip
            Returns:
             none
    """
    try:
        username = "l00163278"
        password = "Qwerty123$"

        print("Establishing a connection...")
        session = paramiko.SSHClient()  # assigning SSH client
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls -al > longList.txt\n")  # unix command to list directory contents and save to file
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was at least one IOS syntax error on device {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException as err:
        print(err)
        print("Authentication Error")


if __name__ == "__main__":
    '''
        Main method of application
        Connection test to a VM using SSH port
        Parameters:
        none
        Returns:
        none
         '''
    ssh_connection("192.168.150.128")
