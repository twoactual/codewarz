#!/usr/bin/python

import subprocess
import sys

path = sys.argv[1]
key = subprocess.check_output([path,'how','deep','does','it','go?']).strip("\n")
print key