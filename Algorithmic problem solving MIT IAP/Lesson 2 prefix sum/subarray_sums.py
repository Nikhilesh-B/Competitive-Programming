import sys

input = sys.stdin.readline

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

psa = [0]*(n+1)

for i in range(1, n+1):
    psa[i] = psa[i-1]+arr[i-1]


saved_sums = {x: 0 for x in psa}
idxs_saved_sums = {x: [] for x in psa}

for i, x in enumerate(psa):
    saved_sums[x] += 1
    idxs_saved_sums[x].append(i)

total_sas = 0

print()
print(f'psa = {psa}')
print(f'saved_sums = {saved_sums}')

for x in psa:
    new_target = target+x
    if new_target in saved_sums:
        total_sas += saved_sums[new_target]

print(total_sas)
