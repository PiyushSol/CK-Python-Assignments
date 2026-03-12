import requests
import time
import logging

urls = [
    "http://www.example.com/nonexistentpage",
    "http://httpstat.us/404",
    "http://httpstat.us/500",
    "https://www.google.com/"
]

logging.basicConfig(
    filename="uptime_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

error_count = {url: 0 for url in urls}


def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code

        print(f"{url} -> Status Code: {status_code}")

        logging.info(f"{url} -> Status Code: {status_code}")

        if 400 <= status_code < 600:
            print(f"ALERT: {url} returned error {status_code}")
            logging.warning(f"ALERT: {url} returned error {status_code}")

            error_count[url] += 1
        else:
            error_count[url] = 0

    except requests.exceptions.RequestException as e:
        print(f"ERROR accessing {url}: {e}")
        logging.error(f"ERROR accessing {url}: {e}")
        error_count[url] += 1

while True:

    for url in urls:
        check_url(url)

    max_errors = max(error_count.values())

    if max_errors > 0:
        interval = min(10 * (2 ** max_errors), 300)  # exponential backoff
    else:
        interval = 10

    print(f"\nNext check in {interval} seconds...\n")

    time.sleep(interval)