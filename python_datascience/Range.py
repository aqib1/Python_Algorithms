if __name__ == '__main__':
    for i in range(1, 5):
        print(i)

    range_list = list(range(5, 25))
    print(range_list)

    print(list(range(10)))

    x = [1, 2, 3, 4, 5]
    power_list = []

    for val in x:
        power_list.append(val**2)

    print("Power list : ", power_list)