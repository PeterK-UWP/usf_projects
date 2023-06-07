import sys

#from log import log
from lammps-logfile import log
if len(sys.argv) < 3:
    raise Exception("Syntax: log2txt.py log.lammps data.txt X Y ...")

logfile = sys.argv[1]
datafile = sys.argv[2]
columns = sys.argv[3:]

print(logfile)
lg = log(logfile)
lg.write(datafile, *columns)
