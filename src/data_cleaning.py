import pandas as pd

def load_data(path: str):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df