import sys
import thread
from socket import*


buff_size = 1024   
if len(sys.argv) < 2 or type(int(sys.argv[1])) != int:
    print("Please, enter an appropiate port number!")
    sys.exit()
serverPort = int(sys.argv[1]) 
def listenToClient(connectionSocket, addr):        #this function is used for the thread
    try:
        getRequest = connectionSocket.recv(buff_size).decode()
       # file = getRequest.split()[1]               #divides the first line
       # f = open(file[1:])                         #opens the path
       # data = f.read()
        response =  getRequest
	print('From Client: ', response)
        #for i in range(0, len(response)):
	if (response == "How are you?"):
		response = "Good and you?"
        mport sys
import thread
from socket import*


buff_size = 1024
if len(sys.argv) < 2 or type(int(sys.argv[1])) != int:
    print("Please, enter an appropiate port number!")
    sys.exit()
serverPort = int(sys.argv[1])
def listenToClient(connectionSocket, addr):        #this function is used for the thread
    try:
        getRequest = connectionSocket.recv(buff_size).decode()
       # file = getRequest.split()[1]               #divides the first line
       # f = open(file[1:])                         #opens the path
       # data = f.read()
        response =  getRequest
        print('From Client: ', response)
        #for i in range(0, len(response)):
        if (response == "How are you?"):
                response = "Good and you?"
        if 'Hello'  in response:
                response = "Hello, this is the server!"
        connectionSocket.send(response.encode()) #encodes and sends the message by chunks
        connectionSocket.send("\r\n".encode())
       #connectionSocket.close()
    except IOError:
        errorMessage = "HTTP/1.1 404 Not Found\r\n\r\n"     #throws an error
        connectionSocket.send(errorMessage.encode())        #sends the error
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)                 #establishes connection
serverSocket.bind(('',serverPort))                          #binds to the port
serverSocket.listen(10)
while True:
    print('Server listening...')
if 'Hello'  in response:
		response = "Hello, this is the server!"  
        connectionSocket.send(response.encode()) #encodes and sends the message by chunks
        connectionSocket.send("\r\n".encode())
       #connectionSocket.close()
    except IOError:
        errorMessage = "HTTP/1.1 404 Not Found\r\n\r\n"     #throws an error
        connectionSocket.send(errorMessage.encode())        #sends the error
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)                 #establishes connection
serverSocket.bind(('',serverPort))                          #binds to the port
serverSocket.listen(10) 
while True:
    print('Server listening...')
    connectionSocket, addr = serverSocket.accept()
    thread.start_new_thread(listenToClient, (connectionSocket, addr))  #creates a new thread

