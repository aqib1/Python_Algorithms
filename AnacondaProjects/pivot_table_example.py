import pandas as pd

if __name__ == '__main__':
    revenue = pd.read_csv('salesmen.csv')
    ## By default, the aggregation function will be mean.
    revenueMeanPivotTable = revenue.pivot_table(values='Revenue', index='Salesman')
    revenueMeanPivotTable.columns = ['Revenue Mean']
    print(revenueMeanPivotTable)

    revenueCountPivotTable = revenue.pivot_table(
        values='Revenue',
        index='Salesman',
        aggfunc='count'
    )
    revenueCountPivotTable.columns = ['Revenue Count']
    print(revenueCountPivotTable)

    revenueColumnMap = {
        'min': 'Revenue Min',
        'max': 'Revenue Max',
        'sum': 'Revenue Sum',
        'median': 'Revenue Median'
    }
    revenueAggPivotTable = revenue.pivot_table(
        values='Revenue',
        index='Salesman',
        aggfunc={'Revenue' : ['min', 'max', 'sum', 'median']}
    )
    revenueAggPivotTable.columns = [
        revenueColumnMap[col] for col in revenueAggPivotTable.columns
    ]
    print(revenueAggPivotTable)