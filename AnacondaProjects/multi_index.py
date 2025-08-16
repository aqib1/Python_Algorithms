import pandas as pd
if __name__ == '__main__':
    df = pd.read_csv('fortune1000.csv')
    print(df.head())

    print("==============")
    print(df.info())
    df['Sector'] = df['Sector'].astype('category')
    print(df.info())

    print("==============")
    rankIndex = df.set_index('Rank')
    print(rankIndex)

    print("==============")
    ## Sector 21
    ## Industry 73
    print(df.nunique())
    multiIndex = df.set_index(keys=['Sector', 'Industry']).sort_index()
    print(multiIndex)
    print(multiIndex.index.names)