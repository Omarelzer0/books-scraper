import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


# lists
titles = []
prices = []
ratings = []
instock = []
URLs = []


base_url = "https://books.toscrape.com/"  # for full url

for page in range(1, 6):  # bc we need 5 pages
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    src = response.content
    soup = BeautifulSoup(src, "html.parser")

    # start scraping
    book_titles = soup.find_all("h3")
    book_prices = soup.find_all("p", {"class": "price_color"})
    book_ratings = soup.find_all("p", {"class": "star-rating"})
    instock_availability = soup.find_all(
        "p", {"class": "instock availability"}
    )
    book_urls = soup.find_all("div", {"class": "image_container"})

    for item in range(len(book_titles)):
        title = book_titles[item].a.get("title")
        titles.append(title)

        price = book_prices[item].text
        prices.append(price)

        rating = book_ratings[item].get("class")[1]
        ratings.append(rating)

        stock = instock_availability[item].text.strip()
        instock.append(stock)

        url = urljoin(base_url, book_urls[item].a.get("href"))
        URLs.append(url)  # this is full url


data = {
    "title": titles,
    "price": prices,
    "rating": ratings,
    "in_stock": instock,
    "url": URLs
}

df = pd.DataFrame(data)


# convert price to numeric value
df["price"] = df["price"].str.replace("£", "").astype(float)


# convert instock to true or false
df["in_stock"] = df["in_stock"].map({
    "In stock": True,
    "Out of stock": False
})


# rating as 1–5, not a word
df["rating"] = df["rating"].map({
    "Three": 3,
    "One": 1,
    "Four": 4,
    "Five": 5,
    "Two": 2
})


print(f"Scraped {len(df)} books")
df.info()


# turn it to csv file without df's index
df.to_csv("books.csv", index=False)