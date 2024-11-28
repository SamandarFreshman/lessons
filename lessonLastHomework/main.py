import schedule
import time
import subprocess
from recording import recording

def run_target_script():
    try:
        subprocess.run(["python", "inspection.py"], check=True)
    except Exception as e:
        recording(f"Error running target script: {e}")

schedule.every().day.at("09:00").do(run_target_script)

recording("Scheduler started. Waiting for the scheduled time...")
while True:
    schedule.run_pending()
    time.sleep(1)
