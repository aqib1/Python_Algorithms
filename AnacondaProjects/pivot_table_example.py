import pandas as pd

if __name__ == '__main__':
    revenue = pd.read_csv('salesmen.csv')
    revenuePivotTable = revenue.pivot_table(values='Revenue', index='Salesman')
    print(revenuePivotTable)