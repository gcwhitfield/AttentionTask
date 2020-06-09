'''
George Whitfield
gwhitfie@andrew.cmu.edu
June 9, 2020

server.py - server for the attention task.

How to use this file:

    python3 server.py

    This will create a server that runs forever until a CTRL + C signal is 
    received.
'''

import socketserver
import string

# starter code is copied from the python documentation about socketserver
# https://docs.python.org/3/library/socketserver.html

class AttentionTaskServer(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        print("yay i'm handling the connection :)")
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} wrote: {self.data}")

        # send back the same data, but all uppsercased
        self.request.sendall(self.data.upper())
        return

'''
1) creates a server on localhost and port 9999
2) reads the data that is sent to the sevrer
3) sends the same data back to the client, but uppercased
'''
def main():
    if __name__ == "__main__":
        HOST, PORT = "localhost", 9999
        # connect the server to localhost on port 9999
        print("Creating server on host {HOST} and port {PORT}.")
        with socketserver.TCPServer((HOST,PORT), AttentionTaskServer) as server:
            # server will run forever until someone hits CTRL + C
            print("Serving forever...")
            server.serve_forever()
        print("Server killed.")
    return

main()