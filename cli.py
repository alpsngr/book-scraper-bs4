import argparse
import sys
import time
import os
from requests.exceptions import HTTPError
from bs4_scraper.runner import scrape_books
from bs4_scraper.storage import save_csv, save_json, save_excel

def main():
    parser = argparse.ArgumentParser(
        description="Book Scraper CLI: crawl books.toscrape.com with pagination support"
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Starting URL (e.g. http://books.toscrape.com/)"
    )
    parser.add_argument(
        "--formats",
        default="csv",
        help="Comma‑separated output formats: csv, json, excel"
    )
    parser.add_argument(
        "--output",
        default="output",
        help="Output directory (default: output)"
    )
    args = parser.parse_args()

    # Create output folder if it doesn't exist
    os.makedirs(args.output, exist_ok=True)

    # Run scraper and handle HTTP errors
    try:
        books = scrape_books(args.url)
    except HTTPError as error:
        status = error.response.status_code if error.response else "?"
        print(f"⚠️  Failed to fetch data: HTTP {status}")
        sys.exit(1)

    # Save results according to requested formats
    requested = [fmt.strip().lower() for fmt in args.formats.split(",")]
    if "csv" in requested:
        save_csv(books, os.path.join(args.output, "books.csv"))
    if "json" in requested:
        save_json(books, os.path.join(args.output, "books.json"))
    if "excel" in requested or "xlsx" in requested:
        save_excel(books, os.path.join(args.output, "books.xlsx"))

    print("✅ Done! Files have been saved to", args.output)

if __name__ == "__main__":
    start = time.time()
    main()
    duration = time.time() - start
    print(f"⏱ Total elapsed time: {duration:.2f} seconds")
