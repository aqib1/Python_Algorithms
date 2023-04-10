import pandas as pd

if __name__ == '__main__':
    foods = pd.read_csv('restaurant_foods.csv')
    customers = pd.read_csv('restaurant_customers.csv')
    week1 = pd.read_csv('restaurant_week_1_sales.csv')
    week2 = pd.read_csv('restaurant_week_2_sales.csv')

    print(foods.head())
    print(week1.head())

    merged = week1.merge(foods, how='left', on='Food ID')
    print(merged)

    print("===========================")
    ## In case of different columns
    print(customers.head())
    customerMerged = week1.merge(
        customers,
        how='left',
        left_on='Customer ID',
        right_on='ID'
    ).drop('ID', axis='columns') ## as ID and Customer ID both are repeated
    print(customerMerged.head())