#!/usr/bin/env python3
#W zadanym katalogu przerób wszystkie dowiązania symboliczne 
# wskazujące na pliki regularne (do których wykonujący skrypt 
# nie ma prawa zapisu), tak aby ścieżki w dowiązaniach były 
# bezwzględne.

import os
import sys
from os.path import join

if len(sys.argv)!=2:
    print("Liczba argumentow jest niepoprawna")
else:
    if os.path.isdir(sys.argv[1]):
        for root, dirs, files in os.walk(sys.argv[1]):
            for file in files:
                myFile = join(os.path.abspath(root), file)
                if os.path.islink(myFile):
                    myPath = os.path.abspath(os.path.realpath(myFile))
                    if os.path.isfile(myPath) and not os.access(myPath, os.W_OK):
                        os.remove(myFile)
                        os.symlink(myPath, myFile)
        
