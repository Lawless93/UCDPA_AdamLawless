import pandas as pd


# Function to import and format Crypto Price file
def read_format(filename):
    df = pd.read_csv(filename)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Date"] = df["Date"].dt.to_period("M")
    df = df.groupby(df["Date"], as_index=False).mean()
    return df


# Function to merge Crypto Price files and drop NaNs
def merge_data(df1, df2, on, name1, name2):
    df = df1.merge(df2, on=on, how="left", suffixes=(name1, name2))
    df = df.dropna(axis=0, how="any")
    return df
