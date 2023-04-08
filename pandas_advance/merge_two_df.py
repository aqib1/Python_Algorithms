import pandas as pd

if __name__ == '__main__':
    foods = pd.read_csv('restaurant_foods.csv')
    customers = pd.read_csv('restaurant_customers.csv')
    week1 = pd.read_csv('restaurant_week_1_sales.csv')
    week2 = pd.read_csv('restaurant_week_2_sales.csv')

    print(week1.head())