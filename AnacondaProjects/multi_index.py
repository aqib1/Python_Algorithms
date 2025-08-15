import pandas as pd
if __name__ == '__main__':
    df = pd.read_csv('fortune1000.csv')
    print(df.head())

    print("==============")
    df = df.set_index('Rank')
    print(df.info())

    print("==============")
    df['Sector'] = df['Sector'].astype('category')
    print(df.info())