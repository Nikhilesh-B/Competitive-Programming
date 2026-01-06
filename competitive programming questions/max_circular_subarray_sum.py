class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mx = -1*float('inf')
        n = len(nums)

        # kadandes
        mx_val = max(nums)
        all_neg = True

        for num in nums:
            if num >= 0:
                all_neg = False
                break

        if all_neg:
            return mx_val

        csum = 0
        for j, num in enumerate(nums):
            csum = max(num+csum, 0)
            mx_val = max(mx_val, csum)

        lsum = [0 for _ in range(n)]
        rsum = [0 for _ in range(n)]

        for i, num in enumerate(nums):
            if i == 0:
                lsum[i] = num
                continue
            lsum[i] = lsum[i-1]+num

        print(f"Left sums (excluding the element at that value) = {lsum}")

        nums.reverse()
        for j, num in enumerate(nums):
            if j == 0:
                rsum[j] = num
                continue
            rsum[j] = rsum[j-1]+num
        rsum.reverse()

        print(f"Right sums (excluding the element at that value) = {rsum}")

        nums.reverse()
        for i, num in enumerate(nums):
            mx_val = max(mx_val, num+lsum[i]+rsum[i])

        agg_lsum = []
        agg_rsum = []

        for i, ls in enumerate(lsum):
            if not agg_lsum:
                agg_lsum.append(ls)
            else:
                agg_lsum.append(max(agg_lsum[-1], ls))

        nums.reverse()
        rsum.reverse()

        for i, rs in enumerate(rsum):
            if not agg_rsum:
                agg_rsum.append(rs)
            else:
                agg_rsum.append(max(agg_rsum[-1], rs))

        nums.reverse()
        rsum.reverse()
        agg_rsum.reverse()

        for i in range(n):
            mx_val = max(mx_val, agg_lsum[i]+agg_rsum[i])

        print("Agg ls", agg_lsum)
        print("Agg rs", agg_rsum)

        return mx_val
