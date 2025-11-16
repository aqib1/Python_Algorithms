class Solution:
    def pow(self, value, n):
        return value**n

    def split_str(self, value: str):
        return value.split()

    def domain_get(self, email):
        return email.split('@')[1]

    def find_dog(self, sentence: str):
        return sentence.lower().__contains__("dog")

    def count_dog(self, sentence: str):
        dog_count = 0
        sentence = sentence.lower()
        for data in sentence.split():
            if data.__eq__("dog"):
                dog_count += 1
        return dog_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.pow(7, 4))
    print(solution.split_str("Hi there Sam!"))

    planet = "Earth"
    diameter = 12742
    print("The diameter of {} is {} kilometers.".format(planet, diameter))

    lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
    print(lst[3][1][2][0])

    d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
    print(d['k1'][3]['tricky'][3]['target'][3])

    domain = solution.domain_get("user@domain.com")
    print(domain)

    print(solution.find_dog('Is there a dog here?'))
    print(solution.count_dog('This dog runs faster than the other dog dude!'))

    seq = ['soup', 'dog', 'salad', 'cat', 'great']
    filtered_list = list(filter(lambda x: x.startswith('s') == False, seq))
    print(filtered_list)