from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("server is already to welcome....")

while True:
    clientSocket, address = serverSocket.accept()
    message_rcv = clientSocket.recv(2048).decode()
    print(f"client says: {message_rcv}; add; {address}")
    clientSocket.send(message_rcv.upper().encode())
    clientSocket.close() #closing the connectiion after sending data 
    break #stopping the server here and closing the connection