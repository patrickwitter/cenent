import random

AgentA_codes = []
AgentB_codes = []

predefined = ["AJK78", "KTV90", "NEL55", "DFG28"]

AgentA = "2975"
AgentB = "6144"

# Write code that will Generate all possible connection codes for the Agents and store them in their respective arrays.
for pre in predefined:
    """Your Code here."""
    AgentA_codes.append(pre+AgentA)
    AgentB_codes.append(pre+AgentB)

questions = [("I saw a purple Kangaroo yesterday, did you?", "Only after the sun went down"),
             ("What did Eve say when she ate the fruit?", "Nothing"),
             ("What do you call a fish wearing a bowtie?", "Sofishticated"),
             ("What did the ocean say to the beach?", "Nothing it just waved"),
             ("Why did God save men but not fallen angels?", "Good Question")]

# This function should return a random instance from the questions array.


def getSecretQuestion():
    """Your Code here."""
    n = random.randint(0, questions.__len__-1)
    return questions[n]

# This function must check the connection code given by the client (Agent) and return the name of the Agent (Agent A or B). If the code is invalid the function should return -1.


def check_conn_codes(connCode):
    """Your Code here."""
    if(len(connCode) == 9):
        pre = connCode[0:5]
        if pre in predefined:
            agent = connCode[5:]
            if(agent == AgentA):
                return "AgentA"
            elif(agent == AgentB):
                return 'AgentB'

    return -1
