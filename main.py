from scraper import scrape_products
from data_cleaning import clean_data
from export_data import export_data

import pandas as pd


def main():

    print("Starting e-commerce scraper...\n")

    # Step 1: Scrape products
    products = scrape_products()

    if not products:
        print("No products were scraped. Stopping program.")
        return

    print("\nTotal products scraped:", len(products))

    # Step 2: Convert into DataFrame
    df = pd.DataFrame(products)

    # Step 3: Clean data
    df = clean_data(df)

    print("\nCleaned product data:")
    print(df.head())

    # Step 4: Display summary
    print("\nTotal cleaned products:", len(df))
    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    # Step 5: Export files
    export_data(df)

    print("\nScraping project completed!")


if __name__ == "__main__":
    main()