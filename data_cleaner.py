import pandas as pd

def cleanData(filepath):
    df = pd.read_csv(filepath)
    df.fillna(0)
    df.columns = df.columns.str.strip()
    if filepath == 'data/country_wise_latest.csv':
        df['Deaths/100 Recovered'] = df['Deaths/100 Recovered'].astype(str).str.replace('inf', '0').astype(float)