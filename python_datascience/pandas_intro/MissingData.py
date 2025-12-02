import pandas as pd
import numpy as np

if __name__ == '__main__':
    data = {
        'A': [1, 2, 3, np.nan],
        'B': [4, np.nan, 5, 6],
        'C': [8, 9, 0, 9]
    }

    df_data = pd.DataFrame(data)
    print(df_data)

    print('*' * 50)
    print(df_data.dropna()) ### Drop rows which have nan values

    print('*' * 50)
    print(df_data.dropna(axis=1))  ### Drop columns which have nan values