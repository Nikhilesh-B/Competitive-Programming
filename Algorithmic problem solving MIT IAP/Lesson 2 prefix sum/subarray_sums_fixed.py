import sys
import random

# Random seed to protect against hash collision attacks
RANDOM = random.randint(1, 10**9)


class SafeDict:
    """Dictionary with randomized hashing to prevent collision attacks"""

    def __init__(self):
        self.data = {}

    def _hash(self, key):
        # Custom hash: XOR with random seed and apply additional mixing
        return (key ^ RANDOM) * 1000000007 % (2**61 - 1)

    def get(self, key, default=0):
        hashed = self._hash(key)
        return self.data.get(hashed, default)

    def __setitem__(self, key, value):
        hashed = self._hash(key)
        self.data[hashed] = value

    def __getitem__(self, key):
        return self.get(key, 0)


# Use buffered read for faster I/O
data = list(map(int, sys.stdin.buffer.read().split()))
n, target = data[0], data[1]
arr = data[2:2+n]

ans = 0
seen = SafeDict()
seen[0] = 1  # Empty prefix has sum 0
prefix = 0

for x in arr:
    prefix += x
    # Count subarrays ending at current position with sum = target
    ans += seen[prefix - target]
    current_count = seen[prefix]
    seen[prefix] = current_count + 1

print(ans)
