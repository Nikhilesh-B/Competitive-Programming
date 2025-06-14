from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        min_days = min(bloomDay)
        mx_days = max(bloomDay)
        last_valid = 0

        while min_days < mx_days:
            mid_days = (min_days+mx_days+1)//2
            possible = self.checkPossible(bloomDay, mid_days, m, k)
            if possible:
                last_valid = mid_days
                mx_days = mid_days-1
            else:
                min_days = mid_days

        if last_valid:
            return last_valid

        else:
            return -1

    def checkPossible(self, bloomDay, val, m, k):
        flags = [0 if bloom > val else 1 for bloom in bloomDay]

        counts = 0
        consecutive = 0

        for i in range(len(flags)):
            if flags[i] == 1:
                consecutive += 1
            else:
                consecutive = 0

            if consecutive == k:
                counts += 1
                consecutive = 0

        if counts >= m:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()