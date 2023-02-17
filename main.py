import os
from typing import *
import logging
from time import sleep
import subprocess
from cs_task import CSTask
import argparse

# parse the command options
parser = argparse.ArgumentParser()
parser.add_argument("-c", type=str, help="specify the config file")
args = parser.parse_args()
config = args.c if args.c != None else ""

cstask = CSTask(config)

# logging init
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s')

file_path = r"C:\Users\ming\projects\code-sentry\raw.txt"

# prompt information
logging.info(f'"{cstask.name}" task is started')
logging.info(f'the files is watched')
logging.info(f'the commands is being executing')

file_paths = cstask.get_file_paths_watched()
scripts: List[str] = cstask.scripts

lastest_modified_time = .0

while True:

    # upadate the latest time of file modified and execute the scripts
    for file_path in file_paths:
        current_file_modified_time = os.stat(file_path).st_mtime
        if current_file_modified_time > lastest_modified_time:
            # TODO exec the script
            for script in scripts:
                os.system(script)
            lastest_modified_time = current_file_modified_time

    # set scan time
    sleep(1)
