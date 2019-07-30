## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("./testdir"))

# Let us check if this file is indeed a file!
print (os.path.isfile("testdir/t1.c"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))