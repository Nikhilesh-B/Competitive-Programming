import bisect
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        prices = price
        prices.sort()
        max_tastiness = prices[-1]-prices[0]
        min_tastiness = 0
        last_valid_tastiness = 0
        while min_tastiness < max_tastiness:
            mid_tastiness = (min_tastiness + max_tastiness + 1) // 2
            possible = self.isPossible(mid_tastiness, prices, k)
            if possible:
                min_tastiness = mid_tastiness
                last_valid_tastiness = mid_tastiness
            else:
                max_tastiness = mid_tastiness-1

        if last_valid_tastiness:
            return last_valid_tastiness
        else:
            return min_tastiness

    def isPossible(self, mid_tastiness, prices, k):
        cval = prices[-1]
        k = k-1
        while k:
            find_val = cval-mid_tastiness
            insertion_point = bisect.bisect_left(prices, find_val)
            if prices[insertion_point] == find_val:
                cval = prices[insertion_point]
                k -= 1
                continue
            else:
                new_curr_idx = insertion_point-1
                if new_curr_idx == -1:
                    return False
                cval = prices[new_curr_idx]
                k -= 1
        return True


if __name__ == "__main__":
    prices = [13, 5, 1, 8, 21, 2]
    k = 3
    solution = Solution()
    print(solution.maximumTastiness(prices, k))
