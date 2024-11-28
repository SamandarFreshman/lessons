from dotenv import load_dotenv
import os
import time
load_dotenv()

file = os.environ.get('HISTORY')

def recording(msg):
    with open(file, 'at') as f:
        f.write(time.datetime.gettimenow()+msg+"\n")