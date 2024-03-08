# Tyler Sabin
# CNE 335 Winter Quarter 2024
# 3/7/2024
# source forked from https://github.com/krhodesrtc/CNE335_automation_project.git
# source used from Tyler Sabin's fork https://github.com/tsabin2023/CNE335_automation_project.git
# instructions to complete code https://rtc.instructure.com/courses/2439011/assignments/31799071?module_item_id=79647034
# source of further instructions Kim Rhodes
# # source Brian Huang

import os
class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        check_response = os.system(f"ping -n 5 {self.server_ip}")
        if check_response == 0:
            return True
        else:
            return False
