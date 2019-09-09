import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirects = "127.0.0.1"
website_lists = ["www.facebook.com", "facebok.com", "www.youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
    else:
        print("Fun hours...")

    print(1)
    time.sleep(5)
