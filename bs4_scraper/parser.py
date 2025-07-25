# scraper/parser.py

from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_book_cards(soup):
    """
    Extract a list of <article class="product_pod"> Tag objects
    directly from a BeautifulSoup `soup` object.
    """
    # Önceki hali (gerek kalmadı):
    # soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("article", class_="product_pod")


def extract_book_data(card, base_url):
    """
    Given one `<article>` Tag and a base URL,
    extract title, detail link, price, availability, and image URL.
    Return as a dict.
    """
    title       = card.h3.a["title"]
    href        = card.h3.a["href"]
    detail_link = urljoin(base_url, href)
    price       = card.find("p", class_="price_color").get_text()
    availability= card.find("p", class_="instock availability").get_text(strip=True)
    img_src     = card.find("img")["src"]
    img_url     = urljoin(base_url, img_src)

    return {
        "title":        title,
        "detail_link":  detail_link,
        "price":        price,
        "availability": availability,
        "img_url":      img_url
    }
