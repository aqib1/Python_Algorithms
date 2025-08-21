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


    quarters = pd.read_csv(
        'quarters.csv',
        parse_dates=['Date'],
        date_format='%m/%d/%Y',
        index_col=['Date', 'Salesman']
    ).sort_index()
    print(quarters.head())
    quarters.index.set_names(names="Sale Date", level=0, inplace=True)
    quarters.index.set_names(names="Name", level=1, inplace=True)
    print(quarters.head())

    ## with one line
    quarters.index.set_names(names=["Date", "Salesman"], inplace=True)
    print(quarters.head())

    ## sorting
    print(quarters.sort_index(ascending=[True, False]))

    print(quarters)
    print(quarters.loc[('1/2/2025', 'Cindy') : ('1/2/2025', 'Rob')])