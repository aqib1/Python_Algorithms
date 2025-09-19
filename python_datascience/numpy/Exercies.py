import numpy as np

class Solution:
    def create_zeros(self, n, dtype):
        return np.zeros(n, dtype)

    def create_ones(self, n, dtype):
        return np.ones(n, dtype)

    def create_fives(self, n, dtype):
        return self.create_ones(n, dtype) * 5

    def create_array(self, start = 0, end = 10):
        return np.arange(start, end)

    def create_identity(self, x = 0, y = 0, dtype = float):
        return np.eye(x, y, dtype=dtype)

    def generate_random(self, limit = 1):
        return np.random.rand(limit)

    def generate_random_normal_distribution(self, limit):
        return np.random.randn(limit)

    def generate_lin_space(self, start, stop, n):
        return np.linspace(start, stop, n)

if __name__ == '__main__':
    solution = Solution()
    print(solution.create_zeros(10, float))
    print(solution.create_ones(10, float))
    print(solution.create_fives(10, float))
    array_50 = solution.create_array(10, 51)
    print(array_50)
    print(array_50[array_50 % 2 == 0])
    print(solution.create_array(0, 9).reshape(3, 3))
    print(solution.create_identity(3, 3, int))
    print(solution.generate_random())
    print(solution.generate_random_normal_distribution(25))
    print(solution.create_array(1, 101).reshape(10, 10) / 100)
    print(solution.generate_lin_space(0, 1, 20))

    print("*"*80)
    print("*" * 80)
    print("*" * 80)
    mat = solution.create_array(1, 26).reshape(5,5)
    print(mat)

    print("*" * 80)
    sub_arr = mat[2:,1:].copy()
    print(sub_arr)
    print(sub_arr[1,3])

    print("*" * 80)
    sub_arr1 = mat[0:3, 1:2].copy()
    print(sub_arr1)

    print("*" * 80)
    sub_arr2 = mat[4:5, 0:].copy()
    print(sub_arr2)

    print("*" * 80)
    sub_arr3 = mat[3:, 0:].copy()
    print(sub_arr3)
