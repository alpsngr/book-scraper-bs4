# Book Scraper (Requests + BeautifulSoup)

A robust CLI-based book scraper that crawls [books.toscrape.com](http://books.toscrape.com) with full pagination support. Exports data to CSV, JSON, and Excel formats, and includes retry, proxy, and elapsed-time features.

## 🔧 Features

- **Full Pagination**: Automatically follows the “Next” link across all pages.
- **Data Extraction**: Grabs book title, price, availability, detail URL, and image URL.
- **Multi-format Output**: Save results as CSV, JSON, or Excel (`.xlsx`).
- **Retry Strategy**: Retries up to 5 times on transient HTTP errors (429, 500, 502, 503, 504) with exponential backoff.
- **Proxy Support**: Optional proxy pool—rotate through proxies to mask your IP.
- **Elapsed Time Reporting**: Prints total execution time when the scrape completes.
- **Error Handling**: Gracefully reports HTTP errors and exits with a clear message.

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/book-scraper-bs4.git
   cd book-scraper-bs4
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   # source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the CLI tool with your desired parameters:
```bash
python cli.py \
  --url http://books.toscrape.com/ \
  --formats csv,json,excel \
  --output ./output
```

- `--url` (required): Starting page URL.
- `--formats`: Comma-separated list (`csv`, `json`, `excel`). Default: `csv`.
- `--output`: Output directory (default: current folder `.`).

Once complete, you’ll see:
```
✅ Done! Files have been saved to ./output
⏱ Total elapsed time: XX.XX seconds
```

## 📦 Docker

1. Build the Docker image:
   ```bash
   docker build -t book-scraper .
   ```
2. Run inside a container, mapping host folder to `/data`:
   ```bash
   docker run --rm \
     -v /absolute/path/to/output:/data \
     book-scraper \
     --url http://books.toscrape.com/ \
     --formats csv,json,excel \
     --output /data
   ```
3. Results (`books.csv`, `books.json`, `books.xlsx`) will appear in your specified host folder.

## 📄 Configuration

- **Proxy Pool**: Edit `bs4_scraper/fetcher.py` → `PROXIES` list to add your `http://user:pass@host:port` entries.
- **Retry Settings**: Customize `total`, `backoff_factor`, and `status_forcelist` in the same file.

## 🚧 Contributing

1. Fork the repo and create your feature branch (`git checkout -b feature/your-feature`).
2. Commit your changes (`git commit -m "Add ..."`) 
3. Push to the branch (`git push origin feature/your-feature`).
4. Open a Pull Request.

Please ensure your code follows PEP8 and includes tests for new functionality.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
