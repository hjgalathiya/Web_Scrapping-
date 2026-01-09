import requests
from bs4 import BeautifulSoup
import csv
import sqlite3

BASE_URL = "https://quotes.toscrape.com/page/{}/"

# SQLite DB
conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT UNIQUE,
    author TEXT,
    tags TEXT,
    author_profile TEXT
)
""")

conn.commit()

# CSV file
csv_file = open("quotes.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csv_file)
writer.writerow(["quote", "author", "tags", "author_profile"])

for page in range(1, 11):  # 10 pages
    url = BASE_URL.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        quote_text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tags = ",".join([tag.text for tag in q.find_all("a", class_="tag")])
        profile = q.find("a")["href"]
        profile_url = "https://quotes.toscrape.com" + profile

        # Save CSV
        writer.writerow([quote_text, author, tags, profile_url])

        # Save SQLite (avoid duplicate quotes)
        try:
            cursor.execute("""
            INSERT INTO quotes (quote, author, tags, author_profile)
            VALUES (?, ?, ?, ?)
            """, (quote_text, author, tags, profile_url))
        except sqlite3.IntegrityError:
            pass

    print(f"Scraped page {page}")

conn.commit()
conn.close()
csv_file.close()

print("Scraping completed!!!")
