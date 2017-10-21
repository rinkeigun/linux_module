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
import shutil
from pathlib import Path
Path("b.txt").touch()


args = sys.argv

#files = os.listdir( args[1] )
files = glob.glob( args[1] )
for file in files:
	print( file )

os.mkdir("mydir")
os.makedirs("mydir2/aaa/bbb/ccc")

os.remove("afile.txt")
os.rmdir("adir")

shutil.rmtree("aDirWithSomething")

os.path.exists("a.txt")
os.path.exists("aDir")


os.path.isfile("a.txt")
os.path.isdir("aDir")

os.path.join("aaa", "bbb", "ccc", "afile.txt" )   # aaa/bbb/ccc/afile.txt

os.path.basename("mydir/sub/ddd.txt") #ddd.txt

os.path.dirname("mydir/sub/ddd.txt") #mydir/sub

root, ext = os.path.splitext( "/var/log/myapp/aaa.log") #/var/log/myapp/aaa log
os.path.abspath(".") # /Users/mydir/work
os.path.isabs("/var/log") # True

# last access date
os.path.getatime("a.txt")

#last update date
os.path.getmtime("a.txt")

#file size
os.path.getsize("a.txt")

#copy a file
shutil.copyfile("a.txt", "b.txt")

#copy a dir
shutil.copytree("mydir", "mydir3")

#rename a file
shutil.move("a.txt", "d.txt")
#shutil.move("a.txt", "mydir")

#rename a dir
shutil.move("mydir3", "mydir4")

Path("b.txt").touch()

#----------------------------------------------------------
# FileNotFoundError: [Errno 2] No such file or directory: 'a'
# NotADirectoryError: [Errno 20] Not a directory: 'dir.py'


