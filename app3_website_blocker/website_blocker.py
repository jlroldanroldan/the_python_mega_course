import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "\etc\hosts"
redirects = "127.0.0.1"
website_lists = ["www.facebook.com", "facebok.com", "www.youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            print(content)
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirects + " " + website + "\n")
    else:
        print("Fun hours...")

    time.sleep(5)
