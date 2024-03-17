# Tyler Sabin
# CNE 335 Winter Quarter 2024
# 3/16/2024
# source forked from https://github.com/krhodesrtc/CNE335_automation_project.git
# source used from Tyler Sabin's fork https://github.com/tsabin2023/CNE335_automation_project.git
# instructions to complete code https://rtc.instructure.com/courses/2439011/assignments/31799071?module_item_id=79647034
# source of further instructions Kim Rhodes
# source Brian Huang
# source Kim Rhodes

# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall

from Server import Server

def print_program_info():
    # function does a print statement
    # TODO - Change your name
    print("Server Automator v0.1 by Tyler Sabin")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # r for raw file needed, or it won't interpret pem file correctly
    my_aws_ec2_server = Server("34.218.241.208", r"C:\Users\sabin\OneDrive\Desktop\ts_student_cne340_test.pem")
    # TODO - Call Ping method and print the results
    if my_aws_ec2_server.ping():
        print("code successful")
        # runs a command on AWS EC2 instance to update and upgrade and install chromium
        my_aws_ec2_server.run_a_command("sudo apt -y update && sudo apt -y upgrade && sudo apt install -y chromium-browser")
        print("command successful")
