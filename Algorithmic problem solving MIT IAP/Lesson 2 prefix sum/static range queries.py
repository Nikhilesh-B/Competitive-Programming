import sys

input = sys.stdin.readline

n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))
psa = [0]*(n+1)

for i in range(1, n+1):
    psa[i] = psa[i-1]+arr[i-1]

queries = []
for _ in range(q):
    a, b = list(map(int, input().split()))
    val = psa[b]-psa[a-1]
    print(val)
