import pandas as pd

def double(x: int):
    return x*2


if __name__ == '__main__':
    data = pd.DataFrame({
        'col1': [1, 2, 3, 4],
        'col2': [444, 555, 666, 444],
        'col3': ['abc', 'cde', 'efg', 'ijk']
    })

    print(data.head())
    print('*' * 50)

    print(data['col2'].unique())

    print('*' * 50) ## Number of unique values
    print(data['col2'].nunique())

    print('*' * 50) ## How many times unique values occur
    print(data['col2'].value_counts())

    print('*' * 50)
    print(data[data['col1'] > 2])

    print('*' * 50)
    print(data[(data['col1'] > 2) & (data['col2'] == 444)])

    print('*' * 50)
    print(data['col1'].apply(double))

    print('*' * 50)
    print(data['col3'].apply(len)) ## Built-in len fun

    ## x power 2
    print('*' * 50)
    print(data['col1'].apply(lambda x: x**2))

    print('*' * 50)
    print(data.drop('col1', axis=1))

    print('*' * 50)
    print(data.columns)
    print(data.index)

    # Ascending
    print('*' * 50)
    print(data.sort_values(by='col2'))

    print('*' * 50)
    print(data.sort_values(by='col2', ascending=False))


    ## DataFrame of null representing in boolean.
    print('*' * 50)
    print(data.isnull())

    data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
            'B': ['one', 'one', 'two', 'two', 'one', 'one'],
            'C': ['x', 'y', 'x', 'y', 'x', 'y'],
            'D': [1, 3, 2, 5, 4, 1]}

    df = pd.DataFrame(data)
    print(df)

    print('*' * 50)
    print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))