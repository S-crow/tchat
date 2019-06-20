#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

import socket
import select
import sys 


if(len(sys.argv) !=3):
        print """\
This script run a python tchat 

Usage: python server.py <ip address> <port>
"""
        sys.exit() 

        
main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Get input parameters (ip address, port)
ip_address = str(sys.argv[1])
port = int(sys.argv[2])

	
try:
	main_connection.bind((ip_address, port))	
except socket.error:
	print "Connection failed"
	sys.exit()

#nb max clients connections clients
main_connection.listen(5)

print("Listening on port : {}".format(port))


server_on = True
connected_clients = []


while server_on:	
	
	input_connections, wlist, xlist = select.select([main_connection], [], [], 0.10)


	for new_connection in input_connections:
		client_connection, infos_connection = new_connection.accept()
		
		print "Client connected, IP adress %s, port %s" % (infos_connection[0], infos_connection[1]) 
	
		# Add socket to the list of connected clients
		connected_clients.append(client_connection)


	# Listen the list of connected clients with select

	try:
		rlist, wlist, xlist = select.select(connected_clients, connected_clients, [], 0.10)
	except select.error:
		server_on = False
	else:	
		for client_to_read in rlist:
			
			msg_recv = client_to_read.recv(1024).decode()
			print("Recv: {}".format(msg_recv))
			
			for client_to_write in wlist:
				if(client_to_read != client_to_write):
					client_to_write.send(msg_recv)
			
			if (len(msg_recv) == 0 ):
				#server_on = False
				connected_clients.remove(client_to_read)
				client_to_read.close()
				#connected_clients.remove(client_connection)



print("Close connection")

client_connection.close()
main_connection.close()

