#!/usr/bin/env python3

#W zadanym pliku tekstowym należy znaleźć i wylistować na ekran wszystkie 
# liczby zmiennoprzecinkowe o formacie: cyfry części całkowitej, znak 
# kropki dziesiętnej, cyfry części ułamkowej. Nie należy listować liczb 
# z nieznaczącymi zerami na początku lub końcu, ani liczb nie mających 
# żadnej cyfry przed znakiem kropki.


import sys
import re


if len(sys.argv)!=2:
    print("Liczba argumentow jest niepoprawna")
else:
    with open(sys.argv[1],'r') as f:
        data = f.read()
        floating_number = re.findall('[+-]?[1-9][0-9]*\.[0-9]*[1-9]|0\.[0-9]*[1-9]', data)
        for n in floating_number:
            print(n + " is floating point number")          
     
          
    
