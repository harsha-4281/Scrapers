                                         E-commerce Product Scraper

Project Overview

This is a Python-based web scraping project that extracts book information from Books to Scrape.

The scraper collects product information from multiple pages and organizes the extracted data using Pandas.

Features
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

Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- OpenPyXL

Project Structure
ecommerce_scraper/
├── main.py
├── scraper.py
├── data_cleaning.py
├── export_data.py
├── requirements.txt
├── README.md
└── output/


Installation

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


Output
The scraper generates:
- output/products.csv
- output/products.xlsx

Website
Practice website: https://books.toscrape.com/

Disclaimer
This project uses Books to Scrape, a website designed for practicing web scraping. Always respect website terms, robots.txt instructions, rate limits, and applicable laws when scraping other websites.
