import pandas as pd

if __name__ == '__main__':
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                       index=[0, 1, 2, 3])

    df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                       index=[4, 5, 6, 7])

    df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                       index=[8, 9, 10, 11])

    print('*' * 50)
    print(df1)

    print('*' * 50)
    print(df2)

    print('*' * 50)
    print(df1)

    print('*' * 50)
    print(df3)

    print('*' * 50)
    df_concat = pd.concat([df1, df2, df3]) ## Row wise concatenation
    print(df_concat)

    print('*' * 50)
    df_concat = pd.concat([df1, df2, df3], axis=1)  ## Column wise concatenation
    print(df_concat)

    left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})

    right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K4'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})
    print('*' * 50)
    print(left)

    print('*' * 50)
    print(right)

    print('*' * 50)
    ## inner merge will merge only common keys
    print(pd.merge(left, right, how='inner', on='key'))

    print('*' * 50)
    ## outer merge will merge all keys.
    # Keys which do not match will have NaN values
    print(pd.merge(left, right, how='inner', on='key'))

    print('*' * 50)
    ## outer merge will merge all keys.
    # Keys which do not match will have NaN values
    print(pd.merge(left, right, how='left', on='key'))

    left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                         'key2': ['K0', 'K1', 'K0', 'K1'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})

    right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                          'key2': ['K0', 'K0', 'K0', 'K0'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})

    print('*' * 50)
    print(pd.merge(left, right, how='inner', on=['key1', 'key2']))

    print('*' * 50)
    print(pd.merge(left, right, how='outer', on=['key1', 'key2']))

    print('*' * 50)
    print(pd.merge(left, right, how='left', on=['key1', 'key2']))

    print('*' * 50)
    print(pd.merge(left, right, how='right', on=['key1', 'key2']))

    left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                         'B': ['B0', 'B1', 'B2']},
                        index=['K0', 'K1', 'K2'])

    right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                          'D': ['D0', 'D2', 'D3']},
                         index=['K0', 'K2', 'K3'])
    print('*' * 50)
    print(left.join(right))

    print('*' * 50)
    print(right.join(left))

    print('*' * 50)
    print(right.join(left, how='outer'))