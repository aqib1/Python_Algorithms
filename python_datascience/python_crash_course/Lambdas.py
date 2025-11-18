

# def double(val): return val*2 ## Convert this to lambda

double = lambda val: val*2

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    # new_data = list(map(double, data)) ## reference lambdas
    new_data = list(map(lambda val: val*2, data)) ## Direct lambdas
    print(new_data)

    ## Filters using lambdas
    even_list = list(filter(lambda val: val%2 == 0, data))
    print(even_list)