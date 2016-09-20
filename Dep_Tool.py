"""
Tool for packaging python project as EXE and moving it + any required XML and YAML configs to a predefined location

This tool is designed to be run with the starting CWD to be the same as the python script you are packaging.

Info on pyinstaller: http://helloworldbookblog.com/distributing-python-programs-part-2-the-harder-stuff/
"""

import os
from os import path
import subprocess
import sys
import shutil


# --- Config --- #
destination_base = "C:\\Production"
# --- ------ --- #


# Handle arguments
if len(sys.argv) < 2:
    args = ""
    for arg in sys.argv:
        args += str(sys.argv) + ", "
    raise SyntaxError("Must have more arguments. Given arguments: " + args)
source_file = sys.argv[1]


# Package Python Script
# TODO: Consider including config files inside of EXE.
# TODO: This would require modifications to the all projects supported by this tool.
subprocess.call(["pyinstaller", "--onefile", "--clean", source_file])  # "--icon=icon.ico",


# Move packaged program and supporting files to production area.
cwd = os.getcwd()
base_name = path.basename(cwd)
base_dest_dir = path.join(destination_base, base_name)

if path.isdir(base_dest_dir) is False:
    print("Destination directory does not exist. Creating {}.".format(base_dest_dir))
    os.mkdir(base_dest_dir)

source_file_name, source_file_ext = path.splitext(source_file)
for entry in os.scandir(path='./dist'):
    if source_file_name.lower() in entry.name.lower():
        print("Moving {}".format(entry.name))
        dest = path.join(base_dest_dir, entry.name)
        shutil.copy2(entry.path, dest)

#Scan all files in cwd and copy xml and yaml files
for entry in os.scandir():
    name, extension = path.splitext(entry.name)
    if 'example' not in name.lower():
        if '.xml' == extension.lower() or '.yaml' == extension.lower():
            print("Moving {}".format(entry.name))
            dest = path.join(base_dest_dir, entry.name)
            shutil.copy2(entry.path, dest)
