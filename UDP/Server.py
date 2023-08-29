from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("Server ready...")
while True:
    message_rcv, clientAddress = serverSocket.recvfrom(2048)
    message_rcv = message_rcv.decode()
    if message_rcv in {'q', 'Q'}:
        print("Bye...")
        break
    print(f"Client says: {message_rcv}; client address: {clientAddress}")
    message_send = message_rcv.upper()
    serverSocket.sendto(message_send.encode(), clientAddress)
serverSocket.close()