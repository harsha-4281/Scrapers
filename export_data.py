import os


def export_data(df):

    os.makedirs("output", exist_ok=True)

    csv_path = "output/products.csv"
    excel_path = "output/products.xlsx"

    df.to_csv(csv_path, index=False)
    df.to_excel(excel_path, index=False)

    print("\nFiles exported successfully!")
    print("CSV:", csv_path)
    print("Excel:", excel_path)