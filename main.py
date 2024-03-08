# Tyler Sabin
# CNE 335 Winter Quarter 2024
# 3/7/2024
# source forked from https://github.com/krhodesrtc/CNE335_automation_project.git
# source used from Tyler Sabin's fork https://github.com/tsabin2023/CNE335_automation_project.git
# instructions to complete code https://rtc.instructure.com/courses/2439011/assignments/31799071?module_item_id=79647034
# source of further instructions Kim Rhodes
# source Brian Huang

# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Tyler Sabin")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    my_aws_ec2_server = Server("34.222.42.81")
    # TODO - Call Ping method and print the results
    if my_aws_ec2_server.ping():
        print("code successful")
