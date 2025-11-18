if __name__ == '__main__':
    d = {'k1': 1, 'k2': 2}
    print(d)

    d_keys = d.keys()
    print(d_keys)
    key_list = [key for key in d_keys]
    print(key_list)

    d_values = d.values()
    print(d_values)
    values_list = [value for value in d_values]
    print(values_list)

    ## List as stack
    stack = [1, 2, 3, 4]
    print("Last value : {}".format(stack.pop()))
    stack.append(5)
    print(stack)
    print("Last value : {}".format(stack.pop()))
    print(2 in [1, 2, 3, 4, 'This'])
    print('Test' in [1, 2, 3, 4, 'This'])

    x = [(1,2),(3,4),(5,6)]
    for a,b in x:
        print(a*b)