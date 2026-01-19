import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    quotes = []
    authors_links = set()
    url = BASE_URL

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for q in soup.select(".quote"):
            quote = q.select_one(".text").text
            author = q.select_one(".author").text
            tags = [t.text for t in q.select(".tag")]

            quotes.append({
                "quote": quote,
                "author": author,
                "tags": tags
            })

            link = q.select_one("a")["href"]
            authors_links.add(BASE_URL + link)

        next_page = soup.select_one(".next a")
        url = BASE_URL + next_page["href"] if next_page else None

    return quotes, authors_links


def scrape_authors(links):
    authors = []

    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        authors.append({
            "fullname": soup.select_one(".author-title").text.strip(),
            "born_date": soup.select_one(".author-born-date").text.strip(),
            "born_location": soup.select_one(".author-born-location").text.strip(),
            "description": soup.select_one(".author-description").text.strip(),
        })

    return authors


if __name__ == "__main__":
    quotes, author_links = scrape_quotes()
    authors = scrape_authors(author_links)

    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)

    with open("authors.json", "w", encoding="utf-8") as f:
        json.dump(authors, f, ensure_ascii=False, indent=2)

    print("Дані збережено ✅")
