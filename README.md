                                            E-COMMERCE PRODUCT SCRAPER

PROJECT OVERVIEW:

This is a Python-based web scraping project that extracts book information from Books to Scrape.

The scraper collects product information from multiple pages and organizes the extracted data using Pandas.

FEATURES
- Extract product names.
- Extract product prices.
- Extract product ratings.
- Extract product URLs.
- Scrape multiple pages using pagination.
- Clean scraped data using Pandas.
- Convert prices into numeric values.
- Convert ratings into numeric values.
- Remove duplicate products.
- Export cleaned data into CSV and Excel files.
- Handle common HTTP request errors.

TECHNOLOGIES USED
- Python
- Requests
- BeautifulSoup
- Pandas
- OpenPyXL

PROJECT STRUCTURE
ecommerce_scraper/
├── main.py
├── scraper.py
├── data_cleaning.py
├── export_data.py
├── requirements.txt
├── README.md
└── output/


INSTALLATION

Clone the repository:
git clone YOUR_GITHUB_REPOSITORY_URL

Navigate into the project:
cd ecommerce_scraper

Create a virtual environment:
python -m venv .venv

Activate it on Windows:
.venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Run the Project
python main.py


OUTPUT
The scraper generates:
- output/products.csv
- output/products.xlsx

WEBSITE
Practice website: https://books.toscrape.com/

DISCLAIMER
This project uses Books to Scrape, a website designed for practicing web scraping. Always respect website terms, robots.txt instructions, rate limits, and applicable laws when scraping other websites.
