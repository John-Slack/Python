#!/usr/bin/python

import sys

s = sys.stdin.read()
numOfDigits = 0
for c in s:
	if c.isdigit():
		numOfDigits = numOfDigits + 1
print numOfDigits 
