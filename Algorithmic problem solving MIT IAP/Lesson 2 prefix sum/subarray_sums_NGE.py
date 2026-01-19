import sys
import bisect

input = sys.stdin.readline




n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

psa = [0]*(n+1)

for i in range(1, n+1):
    psa[i] = psa[i-1]+arr[i-1]

idxs_saved_sums = {x: [] for x in psa}

for i, x in enumerate(psa):
    idxs_saved_sums[x].append(i)

total_sas = 0

for j, x in enumerate(psa):
    new_target = target+x
    if new_target in idxs_saved_sums:
        relevant_idxs = idxs_saved_sums[new_target]
        n = len(relevant_idxs)
        matches = bisect.bisect_right(relevant_idxs,j)
        total_sas += (n-matches)

print(total_sas)