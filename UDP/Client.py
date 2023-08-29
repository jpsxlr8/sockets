from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message_snd = input("Enter a lowercase message_snd: ")
    clientSocket.sendto(message_snd.encode(), (serverName, serverPort))
    if message_snd in {'q', 'Q'}:
        break
    message_rcw, server_address = clientSocket.recvfrom(2048)
    print(f"Server says: {message_rcw.decode()}; server add: {server_address}")
clientSocket.close()