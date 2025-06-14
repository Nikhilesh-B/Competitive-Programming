from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        differenced_arr = []
        for i in range(n):
            differenced_arr.append(target[i]-nums[i])

        print(differenced_arr)
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.minimumOperations(nums=[3, 5, 1, 2], target=[4, 6, 2, 4]))