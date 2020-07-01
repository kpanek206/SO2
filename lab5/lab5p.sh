#!/bin/bash
#W zadanym drzewie katalogów wylistować nazwy wszystkich plików 
#regularnych, mających jedno z rozszerzeń o postaci „exe” (wielokrotne 
#rozszerzenia to rozszerzenia, od kropki do kropki lub do końca nazwy, 
#gdy plik ma wiele kropek w nazwie).

if [ "$#" != "1" ]
then
	echo "Nieprawidlowa ilosc argumentow"
	exit 1
elif [ ! -d $1 ]
then
	echo "Folder nie istnieje"
	exit 2
fi

find $1 -type f | egrep '\.exe$|.exe.'