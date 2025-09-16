import numpy as np
if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    np_arr = np.arange(0, 11)
    print(arr)
    print(np_arr)
    print(np_arr[7])

    print(np_arr[0:5])
    print(np_arr[:6])
    print(np_arr[2:])
    print(np_arr[2::2])

    # np_arr[0:5] = 100
    # arr[0:5] = 100 ## Error can only be assigned to iterable
    # like a numpy arrangement list
    # print(arr)
    # print(np_arr)

    arr_2d = np.reshape(np.arange(0, 25), (5, 5))
    print(arr_2d)
    print(arr_2d[0,4])
    ## Row 0,1 and all columns
    print(arr_2d[0:2])

    ## Column 0,1 and all columns
    print(arr_2d[:,0:2])

    ## Complex
    print(arr_2d[3:5,2:4])

    ## Broadcasting
    slice_of_arr = np_arr[0:6].copy()
    print(slice_of_arr)

    slice_of_arr[0:3] = 101
    print(slice_of_arr)
    print(np_arr)

    print(np_arr > 5)
    print(np_arr[np_arr > 5])

