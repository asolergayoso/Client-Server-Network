
#Alejandro Soler Gayoso
#Client 

import sys
import time
from socket import *
flag = 0
echo = 0
counter = 0                                      #to differentiate between w/ and without "--ttl" option
buff_size = 1024
if len(sys.argv) == 3 and sys.argv[2].isdigit():
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
elif len(sys.argv) == 4 and sys.argv[1] == '--rtt':
	serverName = sys.argv[2]
	serverPort = int(sys.argv[3])
	flag = 1
elif len(sys.argv) == 4 and sys.argv[1] == '--echo':
	serverName = sys.argv[2]
	serverPort = int(sys.argv[3])
	echo = 1
	message = raw_input('Enter message to echo: ')
elif len(sys.argv) == 5 and sys.argv[1] == '--echo' and  sys.argv[2] == '--rtt':
	serverName = sys.argv[3]
	serverPort = int(sys.argv[4])
	flag = 1
	echo = 1          #turns flag to one, so it will perform an echo operation 
        message = raw_input('Enter message to echo: ')
else:
	print('Error with the input values. Please try again')
	sys.exit()

UA = "HTTPGET 1.1"
if serverName.startswith('http://'):
    serverName = serverName[7:len(serverName)] #to take http:// out of the argument
elif serverName.startswith('https://'):
	serverName = serverName[8:len(serverName)] #to take https:// out of the argument
sep = serverName.find('/')
if sep != -1: 
	Host = serverName[0:sep]                   #this separated the Host from the path by finding the first "/"
	Path = serverName[sep:len(serverName)]    
else:
    Host = serverName	                       #in case there is not additional path, the path will be "/"
    Path = "/"
getRequest = "GET %s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\nUser-Agent: %s\r\n\r\n" %(Path,Host,UA)
initTime = time.time()                        #starts measuring the time
clientSocket = socket (AF_INET, SOCK_STREAM)  #establish connection TCP
clientSocket.connect((Host, serverPort))
if echo == 0:
	clientSocket.send(getRequest.encode())
else:
	clientSocket.send(message.encode())
response = clientSocket.recv(buff_size)
recvTime = time.time()                        #stops measuring the time
rtt_ms = round(recvTime - initTime, 3)        #this calculates the RTT
if flag == 1:
    print('Round Trip Time in ms:',rtt_ms)
print('From Server:', response.decode())
clientSocket.close()                           #closes the conection of the clientSocket
sys.exit()                                     #ends the process

