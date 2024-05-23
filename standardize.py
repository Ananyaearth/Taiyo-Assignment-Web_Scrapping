import pandas as pd

class DataStandardizer:
    def __init__(self):
        pass

    def standardize_data(self, df):
        df["Tender"] = df["Tender"].str.strip().str.title()
        df["Company"] = df["Company"].str.strip().str.title()
        df["Procurement"] = df["Procurement"].str.strip().str.title()
        df["Notice"] = df["Notice"].str.strip().str.title()
        df["Location"] = df["Location"].str.strip().str.title()
        df["Closing"] = pd.to_datetime(df["Closing"], errors='coerce')
        df["Value"] = df["Value"].str.replace(',', '').str.replace('$', '').astype(float, errors='ignore')
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        return df

if __name__ == "__main__":
    df = pd.read_csv("raw_data.csv")
    standardizer = DataStandardizer()
    df = standardizer.standardize_data(df)
    df.to_csv("standardized_data.csv", index=False)
    print("Data standardization completed and saved to standardized_data.csv")
