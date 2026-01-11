import sys
from collections import defaultdict

input = sys.stdin.readline

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))


ans = 0
seen = defaultdict(int)
seen[0] = 1
prefix = 0

for sum in arr:
    prefix += sum
    ans += seen[prefix-target]
    seen[prefix] += 1


print(ans)
