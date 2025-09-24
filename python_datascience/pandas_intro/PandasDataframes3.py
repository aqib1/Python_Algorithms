import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)

if __name__ == '__main__':
    df = pd.DataFrame(
        randn(5, 4),
        ['A', 'B', 'C', 'D', 'E'],
        ['W', 'X', 'Y', 'Z']
    )

    df['SUM'] = df['W'] + df['X'] + df['Y'] + df['Z']
    print(df)

    print('*' * 50)
    ### Index levels
    outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
    inside = [1, 2, 3, 1, 2, 3]
    multi_index = list(zip(outside, inside))
    print(multi_index)
    print('*' * 50)
    multi_index = pd.MultiIndex.from_tuples(multi_index)
    print(multi_index)

    data = pd.DataFrame(randn(6, 3), multi_index, ['A', 'B', 'C'])
    print(data)

    print('*' * 50)
    print(data.loc['G1'].loc[1]['B'])

    print('*' * 50)
    print(data.index.names)
    data.index.names = ['Groups', 'No.']
    print(data)

    print('*' * 50)
    ## Cross-section of rows and columns
    print(data.xs(1, level='No.'))