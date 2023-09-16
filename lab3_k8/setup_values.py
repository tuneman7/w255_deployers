import sys, getopt,os,smtplib,time
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import subprocess
import random
from utility import Utility as util
from pathlib import Path

def main():

    u = util()

    ec_ip_address      = u.get_data_from_file(os.path.join(u.get_this_dir(),"ip_address.txt")).replace("\n", "").replace("\r", "")
    print("ec_ip_address = {}".format(ec_ip_address))
    ec_ip_address_stream  = u.get_data_from_file(os.path.join(Path.cwd().parent.parent,"w205","from_scratch","ip_address.txt")).replace("\n", "").replace("\r", "")
    print("ec_ip_address_stream = {}".format(ec_ip_address_stream))



    l_template_files = ["linux_box.template","wait_for_jn.template"]
    l_shell_files = ["linux_box.sh","wait_for_jn.sh"]

    i = 0 
    while i<len(l_template_files):
        template_file = l_template_files[i]
        shell_file = l_shell_files[i]
        shell_template       = os.path.join(u.get_this_dir(),template_file)
        shell_outfile        = os.path.join(u.get_this_dir(),shell_file)
        shell_template_text  = u.get_data_from_file(shell_template)
        shell_text           = shell_template_text.replace("<ip_address_of_ec2>",ec_ip_address)
        u.write_text_to_file(shell_outfile,shell_text)
        print(shell_outfile)
        i = i +1


    io_dir = os.getenv("IO_DIR")
    if io_dir is not None:
        html_t = os.path.join(io_dir,"pres_organization.html.template")
        html_o = os.path.join(io_dir,"pres_organization.html")
        html_txt = u.get_data_from_file(html_t)
        html_o_txt = html_txt.replace("<vis_project_url>",ec_ip_address).replace("<stream_project_url>",ec_ip_address_stream)
        u.write_text_to_file(html_o,html_o_txt)
        print(html_o)


main()

