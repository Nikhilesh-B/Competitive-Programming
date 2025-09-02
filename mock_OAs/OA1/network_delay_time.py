from typing import List
from heapq import heapify, heappop, heappush
#simple djikstra's algorithm implementation

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        new_times = []
        for (u, v, w) in times:
            new_times.append([u-1,v-1,w])

        times = new_times
        k-=1

        adj_list = {i:[] for i in range(n)}
        weights = dict()
        for (u, v, w) in times:
            adj_list[u].append(v)
            weights[(u, v)] = w


        min_times = [float('inf') for _ in range(n)]
        min_times[k] = 0


        heap = [(weights[(k, neigh)], k, neigh) for neigh in adj_list[k]]
        heapify(heap)


        while heap:
            edge_weight, node_from, node_to = heappop(heap)
            min_times[node_to] = min(min_times[node_to],edge_weight+min_times[node_from])

            new_edges = [(weights[(node_to, neigh)], node_to, neigh) for neigh in adj_list[node_to]]

            for ne in new_edges:
                heappush(heap, ne)

        answer = max(min_times)
        if answer == float('inf'):
            return -1
        else:
            return answer


if __name__ == "__main__":
    # times = [[2,1,1],[2,3,1],[3,4,1]]
    times = [[1,2,1],[2,1,3]]
    n = 2
    k = 2
    s = Solution()
    print(s.networkDelayTime(times=times,n=n,k=k))