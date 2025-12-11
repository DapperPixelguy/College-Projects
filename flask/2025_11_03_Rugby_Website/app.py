from project import create_app
import schedule, threading, time
from keepalive import ping

app = create_app()

def run_scheduler():
    schedule.every(10).minutes.do(ping)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    app.run(debug=True)

    t = threading.Thread(target=run_scheduler, daemon=True)
    t.start()