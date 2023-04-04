import pandas as pd

if __name__ == '__main__':
    foods = pd.read_csv('restaurant_foods.csv')
    customers = pd.read_csv('restaurant_customers.csv')
    week1 = pd.read_csv('restaurant_week_1_sales.csv')
    week2 = pd.read_csv('restaurant_week_2_sales.csv')

    print('==================================')
    weeks = pd.concat([week1, week2]).sort_index()
    print(weeks) ## this will not change indexes
    # of both dataframes so we will have repeated index. This is because of
    # ignore_index = False property

    print('==================================')
    weeksWithNewIndex = pd.concat([week1, week2], ignore_index=True).sort_index()
    print(weeksWithNewIndex)

    print('==================================')
    weeksWithMultiIndex = pd.concat([week1, week2], keys=['Week 1', 'Week 2'])
    print(weeksWithMultiIndex)

