import sys

input = sys.stdin.readline

n = int(input())

lo, hi = 1, n**2

# Find the median element (middle element for odd n)
k = (n**2 + 1) // 2


def count_less_or_equal(cand):
    """Count how many values in the multiplication table are <= cand"""
    count = 0
    for i in range(1, n+1):
        count += min(cand // i, n)
    return count


# Binary search for the smallest value where count >= k
while lo < hi:
    mid = (lo + hi) // 2
    count = count_less_or_equal(mid)

    if count < k:
        lo = mid + 1
    else:
        hi = mid

print(lo)
