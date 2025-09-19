import os
import sys

def restart_program():
    os.execl(sys.executable, sys.executable, *sys.argv)
