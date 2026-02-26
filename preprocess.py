import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    df['genres'] = df['genres'].str.replace('|', ' ', regex=False)
    df['year'] = df['title'].str.extract(r'\((\d{4})\)')

    # genre weighting
    df['tags'] = (
        df['genres'] + " " +
        df['genres'] + " " +
        df['year'].fillna('')
    )

    return df