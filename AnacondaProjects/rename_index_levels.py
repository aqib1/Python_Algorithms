import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(
        'salesmen.csv',
        parse_dates=['Date'],
        date_format='%m/%d/%Y',
        index_col=['Date']
    ).sort_index()
    print(df.head(10))

    df.index.set_names(names=['Sale Date'], inplace=True)
    print(df.head())
