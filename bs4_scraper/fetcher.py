import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import random

# 1) Define your proxy pool (fill with real proxies)
PROXIES = [
    # "http://user:pass@proxy1.example.com:8080",
    # "http://user:pass@proxy2.example.com:8080",
]

# 2) Session + retry strategy (as before)
session = requests.Session()
retry_strategy = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

def fetch_html(url, timeout=10):
    """
    HTTP GET with retry and optional proxy support.
    If PROXIES list is non‑empty, pick one at random per request.
    """
    # Pick a proxy if available
    if PROXIES:
        proxy = random.choice(PROXIES)
        proxies = {"http": proxy, "https": proxy}
    else:
        proxies = None

    response = session.get(url, timeout=timeout, proxies=proxies)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text
