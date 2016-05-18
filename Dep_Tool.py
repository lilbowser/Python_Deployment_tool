
# import os
import subprocess
import sys


if len(sys.argv) < 2:
    args = ""
    for arg in sys.argv:
        args += str(sys.argv) + ", "
    raise SyntaxError("Must have more arguments: " + args)


subprocess.call(["pyinstaller", "--onefile", "--clean", sys.argv[1]])  # "--icon=icon.ico",

