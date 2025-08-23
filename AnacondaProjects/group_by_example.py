import pandas as pd

if __name__ == '__main__':
    nba = pd.read_csv('nba.csv')
    print(nba.info())
    nba['Position'] = nba['Position'].astype('category')
    print(nba.info())
    print(nba.nunique())
    nba.set_index(keys=['Position', 'Height'], inplace=True)

    print("===============================")
    groupByCollege = nba.groupby('College')
    print(groupByCollege.size())
    print("===============================")
    print(groupByCollege.first())
    print("===============================")
    print(groupByCollege.get_group('Anadolu Efes'))