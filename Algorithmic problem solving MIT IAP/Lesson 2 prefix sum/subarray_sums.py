import sys
from collections import defaultdict

input = sys.stdin.readline


data = list(map(int, sys.stdin.buffer.read().split()))
n, target = data[0], data[1]
arr = data[2:]


class CustomDict(defaultdict):
    def __setitem__(self, key, value):
        custom_key = self.custom_hash(key)
        super().__setitem__(custom_key, value)

    def __getitem__(self, key):
        custom_key = self.custom_hash(key)
        return super().__getitem__(custom_key)

    def __contains__(self, key):
        custom_key = self.custom_hash(key)
        return super().__contains__(custom_key)

    @staticmethod
    def custom_hash(key):
        return key*123 + 456


ans = 0
seen = CustomDict(int)
seen[0] = 1
prefix = 0

for element in arr:
    prefix += element
    ans += seen[prefix-target]
    seen[prefix] += 1


print(ans)
