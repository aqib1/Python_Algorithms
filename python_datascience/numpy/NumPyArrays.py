import numpy as np

## Numpy arrays

## Vectors are 1-d array and Matrices are 2-d arrays
if __name__ == '__main__':
    print("=" * 30)
    my_list = [1, 2, 3]
    print(my_list)

    np_vector = np.array(my_list)
    print(type(np_vector))
    print("=" * 30)

    np_matrices = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )

    print(np_matrices)
    print(type(np_matrices))

    print("=" * 30)

    np_vector_by_range = np.arange(start=0, stop=10, step=2)
    print(np_vector_by_range)

    print("=" * 30)

    np_zeros = np.zeros(3, int)
    print(np_zeros)

    print("="*30)

    np_zeros_2d = np.zeros((4, 3), float, order='F')
    print(np_zeros_2d)

    print("=" * 30)
    np_ones = np.ones(4, int)
    print(np_ones)

    print("=" * 30)
    np_ones = np.ones((4, 3), float)
    print(np_ones)

    print("=" * 30)
    np_lin_space = np.linspace(0, 5, 5)
    print(np_lin_space)

    print("=" * 30)
    ## Eye will generate an identical matrix
    np_eye = np.eye(5)
    print(np_eye)

    ## rand method will return a random number using uniform
    ## distribution (in between 0 and 1).
    print("=" * 30)
    ## 5 random numbers
    np_random = np.random.rand(5)
    print(np_random)

    print("=" * 30)
    ## 5, 5 random 2d-numbers
    np_random_2d = np.random.rand(5, 5)
    print(np_random_2d)

    ## rand method will return a random number using gaussian (normal)
    ## distribution (values can be negative -∞ to +∞).
    print("=" * 30)
    ## 5 random_n ()
    np_random_n = np.random.randn(5)
    print(np_random_n)

    print("=" * 30)
    ## 5, 5 random_n  2d-numbers
    np_random_n = np.random.randn(5, 5)
    print(np_random_n)

    print("=" * 30)
    ## from -100 to 100, choose 10 random integers
    np_random_int = np.random.randint(-100, 100, 10)
    print(np_random_int)

    print("=" * 30)
    arr = np.arange(25)
    print(arr)
    ra_narr = np.random.randint(0, 50, 10)
    print(ra_narr)

    arr_2d = arr.reshape(5, 5)
    print(arr_2d)

    print(ra_narr.max())
    print(ra_narr.min())
    print(ra_narr.argmax())
    print(ra_narr.argmin())

    print("=" * 30)
    print(arr_2d.shape)
    print(arr_2d.dtype)
