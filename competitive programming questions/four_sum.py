import bisect
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        double_sums = []
        for i in range(n):
            for j in range(i+1, n):
                sm = nums[i]+nums[j]
                double_sums.append((sm,i,j))
        
        double_sums.sort(key=lambda x: x[0])

        answers = []
        for s, i, j in double_sums:
            search = target-s
            find = bisect.bisect_left(double_sums, search, key=lambda x:x[0])
            find_val = double_sums[find][0]
            idx1 = double_sums[find][1]
            idx2 =  double_sums[find][2]

            if find_val == search and idx1 != i and idx2 != j:
                answers.append(sorted([nums[i],nums[j],nums[idx1],nums[idx2]]))

        return answers  