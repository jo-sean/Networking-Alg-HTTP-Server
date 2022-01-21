# Name: Sean Perez
# Date: 1/20/2022
# CS 372: Project 1 Part 1
# Sources: Computer Networking A Top-Down Approach Ch. 2.7

from socket import *

def server():
    """Acts as server processing a GET request"""

    # Server is set to localhost and port 4242
    serverName = '127.0.0.1'
    serverPort = 4242

    # Socket created with the variables above and listening for requests
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(1)

    print('Connected by ', serverSocket.getsockname(), '\n')

    # Connected and never ending loop
    while True:

        # Request is received and new socket created
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)

        # Prints what is received and data that will be sent
        print('Received: ', sentence, '\n')
        data = "HTTP/1.1 200 OK\r\n"\
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
            "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

        print('Sending>>>>>>>>', data, '<<<<<<<<\n')

        # Actually sends data to client and closes TCP
        connectionSocket.send(data.encode())
        connectionSocket.close()


if __name__ == "__main__":
    server()



