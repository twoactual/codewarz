#!/usr/bin/python

import subprocess
import sys

path = sys.argv[1]
key = subprocess.check_output([path,'AAA']).strip("\n")
print key