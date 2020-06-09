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
        print("yay i'm handling the connectoin :)")
        return

def main():
    if __name__ == "__main__":
        HOST, PORT = "localhost", 9999
        # connect the server to localhost on port 9999
        with socketserver.TCPServer((HOST,PORT), AttentionTaskServer) as server:
            # server will run forever until someone hits CTRL + C
            server.serve_forever()
    return

main()