from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("connected to server successfully...\n")


message_snd = input("Enter lowercase sentence: ")
clientSocket.send(message_snd.encode())
message_rcv = clientSocket.recv(2048)
print("server says : {message_rcv.decode()}")
clientSocket.close()
