class Conditions:
    def is_event(self, number: int) -> bool:
        if number % 2 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    condition = Conditions()
    print(condition.is_event(12))