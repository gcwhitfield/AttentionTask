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
import asyncio
import websockets

# starter code copied from python documentation about socketserver and sockets
HOST = "localhost"
PORT = 9999

def main_socket():
    data = " ".join(sys.argv[1:]) # data = string of the cmd line args
    print(f"Opening socket on host {HOST} and port {PORT}.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))

        # send the data to the server
        sock.sendall(bytes(data + "\n", "utf-8"))

        #receive response from the server
        resp = str(sock.recv(1024), "utf-8")


    print(f"Sent: {data}")
    print(f"Recieved: {resp}")

async def main_websocket():
    uri = "ws://localhost:1234"
    msg = "potato"
    async with websockets.connect(uri) as websocket:
        await websocket.send(msg)
        print(f"Sending message: {msg}")
        response = await websocket.recv()
        print(f"Here is the response: {response}")
        
asyncio.get_event_loop().run_until_complete(main_websocket())

