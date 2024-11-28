import os
from dotenv import load_dotenv
import json
from recording import recording
load_dotenv()
table = os.environ.get('TABLES')
def load_from_file():
    try:
        notes = []
        with open(table, 'r') as f:
            notes = json.load(f)
    except Exception:
        notes = []
    return notes

def save_to_file(notes):
    try:
        with open(table,'w') as f:
            json.dump(notes, f)
    except Exception as e: 
        recording(f"Error: {e}")