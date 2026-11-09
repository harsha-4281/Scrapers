import pandas as pd


def clean_data(df):

    # Clean product names
    df["product"] = df["product"].astype("string").str.strip()

    # Clean prices
    df["price"] = (
        df["price"]
        .astype("string")
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
        .str.strip()
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Convert ratings into numbers
    rating_mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["rating"] = df["rating"].map(rating_mapping)

    # Remove rows without a product URL
    df = df.dropna(subset=["url"])

    # Remove duplicate products
    df = df.drop_duplicates(subset=["url"])

    return df