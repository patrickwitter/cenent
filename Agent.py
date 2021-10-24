import socket

# Select an appropriate port number.
PORT = 12000
# Set The Server's IP Address
SERVER_IP = socket.gethostname
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

# Add code to initialize the Socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Write Code that will allow the Client (Agent) to send messages to the server. The Function accepts the message as a String (msg) and sends that message to the Server through a connection established.


def send(msg):
    """Your Code here"""

# Write code to Prompts the Agent to enter their connection code and returns the code given.


def getConCode():
    """Your Code here"""

# Write code to Prompts the Agent to enter an answer and returns the answer given.


def getAnswer(question):
    """Your Code here"""


# Get Connection Code.
connCode = getConCode()

# Send Connection Code to Server.
send(connCode)

# Recive question from server.
question = """Your Code here"""

# Get Answer from Agent.
answer = getAnswer(question)

# Send Answer to Server.
send(answer)

# Recive and print response from the server.
"""Your Code here"""
