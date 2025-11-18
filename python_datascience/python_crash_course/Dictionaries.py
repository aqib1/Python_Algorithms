if __name__ == '__main__':
    d = {'key1': 'value', 'key2': 132, 'key3': [1, 2, 3]}
    print(d['key3'][1])

    nested_d = {
        'key1': {
            "k1_1": "Ji",
            "k1_2": [3, 4, 5],
            "k1_3": True
        }
    }

    print(nested_d["key1"]["k1_2"][2])

    t = (1, 2, 3)
    ## t[0] = 132 ## Not possible as tuples are immutables
    print(t)

    list_1 = [1, 2, 3, 1, 1, 1, 3]
    print(list_1)

    set_1 = {1, 2, 2, 2, 2, 3, 3, 4} ## it will return only unique
    print(set_1)

    convert_list1_to_set = set(list_1)
    print(convert_list1_to_set)