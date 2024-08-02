"""
Day 10 - Websocket Command Line Chat
Client
"""

import socket
import threading

HOST = "localhost"
PORT = 777

username = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "USERNAME":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode("utf-8"))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
