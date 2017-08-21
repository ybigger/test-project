import socket

#Create the client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999 # TODO: read the port number from the UI file
clientSocket.connect((host, port))
clientSocket.send('test1.txt'.encode('ascii')) # TODO: read the file name from the UI
serverMessage = clientSocket.recv(1024)

clientSocket.close()

print("%s" % serverMessage.decode('ascii'))
