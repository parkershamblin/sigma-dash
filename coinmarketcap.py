import requests
import pandas as pd


def crypto_market():
    url = "https://coinmarketcap.com/all/views/all/"
    session = requests.Session()
    html = session.get(url).text

    tables = pd.read_html(html)
    df = tables[2]
    df.drop("Unnamed: 10", axis=1, inplace=True)

    # convert percentage change columns to float objects
    for col in ["% 1h", "% 24h", "% 7d"]:
        df[col] = df[col].str.replace("%", "")
        df[col] = df[col].astype(float)

    return df
