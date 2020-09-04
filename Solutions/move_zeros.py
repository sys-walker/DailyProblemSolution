#!/bin/python3

class Solution:
    def moveZeros(self, nums):
        # Fill this in.
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
        for i in range(start, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    Solution().moveZeros(nums)
    print(nums)
    # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
