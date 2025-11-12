def print_data(data = "Default Value"):
    print(data)

def square(num: int) -> int:
    """
    This is a method to find a square of a number
    :param num:
    :return:
    """
    return num**2

if __name__ == '__main__':
    print_data()
    print_data("Test1")
    print_data("Test2")
    print("Square of 3 is {}".format(square(3)))