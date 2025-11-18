if __name__ == '__main__':
    statement = 'This is a string, Its a test string'.upper()
    print(statement.isupper())
    statement_data = statement.split()
    print(statement_data)

    statement = 'This is a string, Its a £test string'
    statement_data = statement.split('£')
    print(statement_data)