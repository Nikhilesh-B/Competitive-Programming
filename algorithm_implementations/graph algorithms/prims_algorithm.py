import heapq


def return_outbound_edges(adj_matrix, u):
    n = len(adj_matrix)
    edges = []
    for v in range(n):
        w = adj_matrix[u][v]
        if w != 0:
            # store as (weight, u, v) for a min-heap
            edges.append((w, u, v))
    return edges


def prims_algorithm(adj_matrix):
    n = len(adj_matrix)
    if n == 0:
        return []

    MST = [[0] * n for _ in range(n)]
    included = [False] * n

    # start from node 0
    included[0] = True
    count_included = 1

    # min-heap of edges crossing the cut
    heap = []
    for edge in return_outbound_edges(adj_matrix, 0):
        heapq.heappush(heap, edge)

    while count_included < n and heap:
        # pop edges that point to an already-included vertex
        while heap and included[heap[0][2]]:
            heapq.heappop(heap)
        if not heap:
            break  # disconnected graph → returns an MST forest for reachable part

        w, u, v = heapq.heappop(heap)
        # add the edge (u, v)
        MST[u][v] = w
        MST[v][u] = w

        if not included[v]:
            included[v] = True
            count_included += 1
            for e in return_outbound_edges(adj_matrix, v):
                heapq.heappush(heap, e)

    return MST


def print_matrix(mat):
    for row in mat:
        print("[ " + " ".join(str(x) for x in row) + " ]")


if __name__ == "__main__":
    adj_matrix = [
        [0, 2, 1, 2, 1],
        [2, 0, 1, 1, 13],
        [1, 1, 0, 2, 12],
        [2, 1, 2, 0, 5],
        [1, 13, 12, 5, 0],
    ]

    mst = prims_algorithm(adj_matrix)
    print_matrix(mst)
