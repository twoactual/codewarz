import subprocess
import sys
import os


path = sys.argv[1]
bins = os.listdir(path)
print bins
for i in bins:
    if not i.endswith("bin"):
        bins.remove(i)

print bins
