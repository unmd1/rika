import recon
import os


def stdin_json():
    pass



def run_command(command):
    
    with os.popen(command) as pse:
        for line in pse:
            print (line)










rc = recon.recon()
