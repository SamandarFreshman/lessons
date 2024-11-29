from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()

file = os.environ.get('HISTORY')

def recording(msg):
    with open(file, 'at') as f:
        f.write("["+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"] "+msg+"\n")