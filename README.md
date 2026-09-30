# Books Scraper

A simple web scraping task using [Books to Scrape](https://books.toscrape.com/).

## Project Structure

```text
books-scraper/
├── scraper.py
├── books.csv
├── queries.sql
└── README.md
```

## Requirements

* Python 3.x
* requests
* BeautifulSoup4
* pandas

Install the required libraries with:

```bash
pip install requests beautifulsoup4 pandas
```

## How to Run

Run the scraper:

```bash
python scraper.py
```

The script scrapes the first 100 books from pages 1–5 and saves the results to `books.csv`.

The CSV contains:

* `title`
* `price`
* `rating`
* `in_stock`
* `url`

The data is also loaded into SQLite and the required SQL queries are provided in `queries.sql`.

## Notes

1. The rating took a little longer than expected because it was stored in the HTML as a CSS class rather than as plain text.
2. The book URLs were relative URLs, so I had to combine them with the base URL to create complete URLs.
3. The scraper worked as expected once I understood the page structure.
4. If the site started blocking requests, I would add a small delay between requests and use retry/backoff logic.
5. I would also avoid unnecessary requests and cache pages if I needed to request them more than once.
