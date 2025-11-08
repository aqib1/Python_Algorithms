class Conditions:
    def is_event(self, number: int) -> bool:
        if number % 2 == 0:
            return True
        else:
            return False

    def print(self, number: int):
        if number == 1:
            print("First")
        elif number == 2:
            print("Second")
        elif number == 3:
            print("Third")
        else:
            print("Unknown")

if __name__ == '__main__':
    condition = Conditions()
    print(condition.is_event(12))
    condition.print(1)