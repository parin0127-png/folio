import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_file(query: str)-> str:
    "open and read the content of any file from the system and return its text"
    path = os.path.join(BASE_DIR, "outputs", query)
    with open(path, "r")as f:
        return f.read()
    
