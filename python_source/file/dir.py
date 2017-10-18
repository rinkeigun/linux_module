# -*- coding: utf-8 -*-

# python3 dir.py path 
# python3 dir.py . 
# python3 dir.py a 
# python3 dir.py dir.py 
# python3 dir.py "../file"
# python3 dir.py "../file/*.*"

import sys
import glob
import os

args = sys.argv

#files = os.listdir( args[1] )
files = glob.glob( args[1] )
for file in files:
	print( file )

#----------------------------------------------------------
# FileNotFoundError: [Errno 2] No such file or directory: 'a'
# NotADirectoryError: [Errno 20] Not a directory: 'dir.py'


