#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

import socket
import sys

if(len(sys.argv) !=3):
        print """\
This script is the client for connecting to the tchat

Usage: python client.py <ip_server> <port>
"""
        sys.exit()

ip_server = str(sys.argv[1])
port_server = int(sys.argv[2])

connect_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect_server.connect((ip_server, port_server))

print("Connected on port {}".format(port_server))

msg_to_send = b""

while msg_to_send != b"end":

	msg_to_send = raw_input("> ").encode() #Encode en UTF-8

	connect_server.send(msg_to_send)

	msg_recv = connect_server.recv(1024)

	print(msg_recv.decode())


print("Close connection")

connect_server.close()

