import sys
input = sys.stdin.readline

N = int(input())
nums = map(int, input().split(" "))

desired_sum = N/2*(N+1)
print(int(desired_sum-sum(nums)))
