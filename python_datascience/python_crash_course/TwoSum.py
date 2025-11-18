from typing import List


class TwoSum:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in target_map:
                return [i, target_map[complement]]
            else:
                target_map[nums[i]] = i

        return []

if __name__ == '__main__':
    twoSum = TwoSum()
    print(twoSum.two_sum([2, 7, 11, 15], 9))