import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)

if __name__ == '__main__':
    df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
    df['SUM'] = df['W'] + df['X'] + df['Y'] + df['Z']
    print(df[df > 0])
    print('*' * 50)
    print(df['W'] > 0)

    print('*' * 50)

    ## python and operator will not work here as it work only with single boolean values
    ## & and | operators will be used for a series of values
    print(df[(df['W'] > 0) & (df['X'] > 0)][['X', 'Y', 'SUM']])
    print('*' * 50)
    print(df[(df['W'] > 0) | (df['X'] > 0)][['X', 'Y', 'SUM']])
    # df.reset_index(inplace=True)
    print('*' * 50)

    states = 'SA CA ED BN MK'.split()
    df['STATES'] = states
    df.set_index('STATES', inplace=True)
    print(df)
