# Tyler Sabin
# CNE 335 Winter Quarter 2024
# 3/16/2024
# source forked from https://github.com/krhodesrtc/CNE335_automation_project.git
# source used from Tyler Sabin's fork https://github.com/tsabin2023/CNE335_automation_project.git
# instructions to complete code https://rtc.instructure.com/courses/2439011/assignments/31799071?module_item_id=79647034
# source of further instructions Kim Rhodes
# source Brian Huang
# source Kim Rhodes

import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_file):
        # TODO -
        # setting up some of our paramiko remote code in the constructor
        self.server_ip = server_ip
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.key = paramiko.RSAKey.from_private_key_file(key_file)

    def ping(self):
        # TODO - Use os module to ping the server
        check_response = os.system(f"ping -n 5 {self.server_ip}")
        if check_response == 0:
            return True
        else:
            return False

    def run_a_command(self, command):
        # creating connection and running command from main
        self.ssh.connect(hostname=self.server_ip, username="ubuntu", pkey=self.key)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        line = stdout.readline()
        while line:
            print(line)
            line = stdout.readline()
        print(stderr.read().decode())
        # closing connection
        self.ssh.close()
        print("ssh connection closed")
