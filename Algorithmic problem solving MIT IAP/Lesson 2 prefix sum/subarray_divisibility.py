import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
mod_seen = defaultdict(int)
prefix_mod = 0
mod_seen[prefix_mod] = 1
print(f"mod_seen ={mod_seen}")

for i, a in enumerate(arr):
    prefix_mod += a
    prefix_mod %= n
    if prefix_mod == 0:
        ans += mod_seen[0]
    else:
        ans += mod_seen[n-prefix_mod]

    print(f"Current idx={i}, current element={a}")
    print(f"prefix mod ={prefix_mod}")
    print(f"mod_seen ={mod_seen}")
    print(f"Answer ={ans}")

    mod_seen[prefix_mod] += 1

print(ans)
