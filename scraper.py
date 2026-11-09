import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"


def scrape_products():

    current_url = BASE_URL
    scraped_data = []

    while current_url:

        print("Scraping:", current_url)

        try:
            response = requests.get(current_url, timeout=15)
            response.raise_for_status()

        except requests.exceptions.RequestException as error:
            print("Request failed:", error)
            break

        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.select("article.product_pod")

        for product in products:

            name_element = product.select_one("h3 a")
            price_element = product.select_one(".price_color")
            rating_element = product.select_one("p.star-rating")

            name = name_element.get("title") if name_element else None
            price = price_element.get_text(strip=True) if price_element else None

            rating_classes = rating_element.get("class", []) if rating_element else []
            rating = rating_classes[1] if len(rating_classes) > 1 else None

            link = name_element.get("href") if name_element else None
            product_url = urljoin(current_url, link) if link else None

            product_data = {
                "product": name,
                "price": price,
                "rating": rating,
                "url": product_url
            }

            scraped_data.append(product_data)

        next_button = soup.select_one("li.next a")

        if next_button:
            next_page = next_button.get("href")
            current_url = urljoin(current_url, next_page)
        else:
            current_url = None

    return scraped_data