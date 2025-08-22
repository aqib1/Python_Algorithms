import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(
        'salesmen.csv',
        parse_dates=['Date'],
        date_format='%m/%d/%Y',
        index_col=['Date']
    )
    print(df.transpose().head())