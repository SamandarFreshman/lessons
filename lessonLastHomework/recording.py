from dotenv import load_dotenv
import os
load_dotenv()

file = os.environ.get('HISTORY')

def recording(msg):
    with open(file, 'at') as f:
        f.write(msg+"\n")