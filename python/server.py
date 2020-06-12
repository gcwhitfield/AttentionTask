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
import asyncio
import websockets
import string

# starter code is copied from the python documentation about socketserver
# https://docs.python.org/3/library/socketserver.html


# ------------ old server code (regular socket connection) ------------------- #
class AttentionTaskState:
    def __init__(self, researcher, child):
        self.researcher = researcher # socket connection
        self.child = child # socket connection
        self.confirm_child = False
        self.confirm_researcher = False
        
        

class AttentionTaskServer(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def __init__(self, *args):
        super().__init__(*args)
        print("yay inti")
        self.task_state = 0


    def handle(self):
        print("yay i'm handling the connection :)")
        self.data = self.request.recv(1024).strip()

        if self.task_state != 0: # task has init
            print("task state has been init")
        else: # wait for the researcher and the child to join
            child = 0
            researcher = 0
            if self.data == "CHILD":
                child = self.request
            elif self.data == "RESEARCHER":
                researcher = self.request
            
            # if both the researcher and the child have been init, create state
            # object
            if child != 0 and researcher != 0:
                self.task_state = AttentionTaskState(researcher, child)
                
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
def main_socket():
    if __name__ == "__main__":
        HOST, PORT = "localhost", 9999
        # connect the server to localhost on port 9999
        print(f"Creating server on host {HOST} and port {PORT}.")
        with socketserver.TCPServer((HOST,PORT), AttentionTaskServer) as server:
            # server will run forever until someone hits CTRL + C
            print("Serving forever...")
            server.serve_forever()
        print("Server killed.")
    return


'''
Sends a message to the researcher and the child once they both have confirmed.
'''
def wait_confirm(server):
    pass


# ------------------- new server code (websockets) --------------------------- #

# websockets code copied from websockets documentation
# https://websockets.readthedocs.io/en/stable/intro.html

async def server(websocket, path):
    msg = await websocket.recv()
    print(f"Here is the msg: {msg}")
    response = msg.upper()
    await websocket.send(response) 

def main_websocket():
    start_server = websockets.serve(server, "localhost", 1234)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

main_websocket()