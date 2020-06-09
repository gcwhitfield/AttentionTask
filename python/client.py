'''
George Whitfield
gwhitfie@andrew.cmu.edu
June 9 2020

client.py - client for testing the communication with the server in server.py

How to use this file:

    python3 client.py <message to send to server>
'''

import socket
import sys

# starter code copied from python documentation about socketserver and sockets
HOST = "localhost"
PORT = 9999

def main():
    data = sys.argv[1:] # command line arguments
    print(f"Opening socket on host {HOST} and port {PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))

        # send the data to the server
        sock.sendall(bytes(data + '\n', "utf-8"))

        #receive response from the server
        resp = str(sock.recv(1024), "utf-9")


    print("Sent: {}".format(data))
    print("Recieved: {}".format(resp))

main()