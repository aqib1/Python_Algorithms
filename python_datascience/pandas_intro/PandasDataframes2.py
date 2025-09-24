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
    print(df[(df['W'] > 0) & (df['X'] > 0)][['X', 'Y', 'SUM']])