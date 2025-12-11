import time
import requests
import schedule, threading


def ping():
    try:
        requests.get('https://college-projects-tslh.onrender.com')
        print('Ping sent')
    except Exception as e:
        print(e)

def run_scheduler():
    schedule.every(10).minutes.do(ping)
    while True:
        schedule.run_pending()
        time.sleep(1)

def run_threader():
    t = threading.Thread(target=run_scheduler, daemon=True)
    t.start()
