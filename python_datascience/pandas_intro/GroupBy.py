import pandas as pd

if __name__ == '__main__':
    # Create dataframe
    data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
            'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
            'Sales': [200, 120, 340, 124, 243, 350]}
    data_df = pd.DataFrame(data)
    print(data_df)

    print('*' * 50)
    ### GroupBy Company and take mean
    print(data_df.groupby('Company')['Sales'].mean())

    print('*' * 50)
    ### GroupBy Company and take sum
    print(data_df.groupby('Company')['Sales'].sum())

    print('*' * 50)
    ### GroupBy Company and take std
    print(data_df.groupby('Company')['Sales'].std())

    print('*' * 50)
    ### GroupBy Company and take a sum of Fb
    print(data_df.groupby('Company')['Sales'].sum()['FB'])

    print('*' * 50)
    ### GroupBy Company and take a count of Person
    print(data_df.groupby('Company')['Person'].count())

    print('*' * 50)
    ### GroupBy Company and take a max sales of person
    ### Note in the person column for MSFT Vanessa will be picked which sales
    ## are less than Amy because Vanessa alphabetically is greater than Amy.
    ## In Sales Amy sale is greater than Vanessa.
    print(data_df.groupby('Company').max())

    ## Correctly pick companies with person have the highest sales.
    print('*' * 50)
    print(data_df.loc[data_df.groupby('Company')['Sales'].idxmax()])

    ## Describe
    print('*' * 50)
    print(data_df.groupby('Company').describe())

    ## Describe + Transpose
    print('*' * 50)
    print(data_df.groupby('Company').describe().transpose())

    ## Describe + Transpose
    print('*' * 50)
    print(data_df.groupby('Company').describe().transpose()['FB'])