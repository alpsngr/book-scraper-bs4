# scraper/runner.py

from .fetcher import fetch_html
from .parser  import parse_book_cards, extract_book_data
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_books(start_url):
    """
    Starting from `start_url`, walk through all pages,
    extract data from each book card, and return a single list of dicts.
    """
    all_books = []
    next_url  = start_url

    while next_url:
        html = fetch_html(next_url)
        soup = BeautifulSoup(html, "html.parser")

        # 1) Find all book cards on this page
        cards = parse_book_cards(soup)
        for card in cards:
            all_books.append(extract_book_data(card, start_url))

        # 2) Look for a "Next" page link; if none, end loop
        next_li = soup.find("li", class_="next")
        if next_li:
            next_url = urljoin(next_url, next_li.a["href"])
        else:
            next_url = None

    return all_books
