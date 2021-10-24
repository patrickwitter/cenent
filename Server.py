import socket
import datetime as dt
import threading
import Verify as av

# Select an appropriate port number.
PORT = 12000
# Set The Server's IP Address
SERVER_IP = socket.gethostname
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

# Add code to initialize the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Write Code to bind Address to the server socket.
"""Your Code here"""
server.bind(ADDR)

# This function processes messages that are read through the Socket.


def clientHandler(conn, addr):
    # Write Code that allows the Server to receive a connection code from an Agent.
    """Your Code here"""
    connCode = conn.recv(1024).decode()
    # Write Code that allows the Server to check if the connection code received is valid.
    """Your Code here"""
    isValidCode = av.check_conn_codes(connCode)
    if(type(isValidCode) is int):  # The only return value that is a integer is -1
        conn.close()
        return
    # Write Code that allows the Server to retrieve a random secret question.
    """Your Code here"""
    question = av.getSecretQuestion()

    # Write Code that allows the Server to send the random secret question to the Client.
    """Your Code here"""
    conn.send(question[0].encode())
    # Write Code that allows the Server to receive an answer from the Client.
    """Your Code here"""
    ans = conn.recv(1024).decode()
    # Write Code that allows the Server to check if the answer received is correct.
    """Your Code here"""
    isValidAns = ans == question[1]
    if(not isValidAns):
        conn.close()
        return
    # Write Code that allows the Server to Send Welcome message to agent -> "Welcome Agent X"
    """Your Code here"""
    date = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    mssg = f"Welcome {isValidCode} Time Logged - <{date}>"
    conn.send(mssg.encode())


def runServer():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=clientHandler, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")


print("[STRTING] The Server is Starting...")
runServer()
