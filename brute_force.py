#!/usr/bin/python
#Book: David Copperfield by Charles Dickens
import sys

f = open(sys.argv[1], "r")

lines = list(f)
theLn = lines[0]
theCh = theLn[0:31]

for shift in range(1,26):	
	for ch in theCh:
		if ord(ch)>=97 and ord(ch)<=122:
			shiftedCh = ord(ch) + shift
			if shiftedCh>122:
				shiftedCh = shiftedCh - 26
			sys.stdout.write(chr(shiftedCh))
		else:
			sys.stdout.write(ch)
	print ""
f.close()
