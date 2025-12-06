import pandas as pd
from sqlalchemy import create_engine

if __name__ == '__main__':
    csv = pd.read_csv('example')
    print(csv.head())

    # csv.to_csv("test", index=False)
    print('*' * 50)
    print('*' * 50)

    xlsx = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')
    print(xlsx)
    #xlsx.to_excel('Excel_Sample2.xlsx', sheet_name='Sheet2')

    print('*' * 50)
    print('*' * 50)
    html = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
    print(html[0])

    print('*' * 50)
    print('*' * 50)
    engine = create_engine('sqlite:///:memory:')
    csv.to_sql('CsvTable', engine)
    csv_from_db = pd.read_sql('CsvTable', con=engine)
    print(csv_from_db)
