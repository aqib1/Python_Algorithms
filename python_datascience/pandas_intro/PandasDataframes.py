import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

if __name__ == '__main__':
    df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
    print(df)
    print("=" * 50)
    ## Grab by column name
    w_column_series = df['W']
    print(w_column_series) ## will return series
    print(type(w_column_series))

    print("=" * 50)
    ### also can be grab using column name directly
    print(df.W)

    print("=" * 50)
    ### get multiple columns (this will return data-frame)
    print(df[['W', 'Z']])

    print("=" * 50)
    ### Generate sum column
    df['SUM'] = df['W'] + df['X'] + df['Y'] + df['Z']
    print(df)

    print("=" * 50)
    ### Drop SUM column (Dropping column will require axis 1, and inplace True will update actual df)
    df.drop('SUM', axis=1, inplace=True)
    print(df)

    print("=" * 50)
    ## Grap a row using row index by label
    print(df.loc['A'])

    print("=" * 50)
    ## Grap a row using row index number
    print(df.iloc[0])

    print("=" * 50)
    ## Grap a row using row index by label and a specific column
    print(df.loc['A', 'Y'])

    print("=" * 50)
    ## Grap a subset using row index by label and a specific column
    print(df.loc[['A', 'B'], ['W', 'Y']])
