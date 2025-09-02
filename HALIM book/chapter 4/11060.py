import sys
import heapq
from heapq import heapify, heappush, heappop

class Drink:
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def __lt__(self, other):
        return self.index < other.index  # preserves original input order on tie

def solve():
    case_number = 1
    lines = sys.stdin.read().splitlines()
    i = 0

    while i < len(lines):
        if lines[i].strip() == "":
            i += 1
            continue

        n = int(lines[i])
        i += 1

        names = []
        idxs = {}
        for j in range(n):
            name = lines[i].strip()
            names.append(name)
            idxs[name] = j
            i += 1

        m = int(lines[i])
        i += 1

        adj_list = {name: [] for name in names}
        indegrees = {name: 0 for name in names}

        for _ in range(m):
            a, b = lines[i].strip().split()
            adj_list[a].append(b)
            indegrees[b] += 1
            i += 1

        # Topological Sort using heap
        heap = []
        for name in names:
            if indegrees[name] == 0:
                heapq.heappush(heap, Drink(name, idxs[name]))

        result = []
        while heap:
            current = heapq.heappop(heap)
            result.append(current.name)
            for neighbor in adj_list[current.name]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    heapq.heappush(heap, Drink(neighbor, idxs[neighbor]))

        print(
            f"Case #{case_number}: Dilbert should drink beverages in this order: {' '.join(result)}.\n")
        case_number += 1


if __name__ == "__main__":
    solve()
