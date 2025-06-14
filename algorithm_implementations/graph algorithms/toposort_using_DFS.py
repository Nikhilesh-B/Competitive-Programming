# directed graph output the topological sorting
graph = [[0, 1, 0, 0],
         [0, 0, 0, 1],
         [0, 1, 0, 1],
         [0, 0, 0, 0]]


def compute_path(explored, node, edge_set, topsort):
    if explored[node]:
        return
    else:
        explored[node] = 1
        if node in edge_set:
            for v in edge_set[node]:
                compute_path(explored, v, edge_set, topsort)
        topsort.append(node)


def do_topsort(g):
    n = len(g)
    explored = [0 for _ in range(n)]
    edges = {}
    topsort = []

    for u, row in enumerate(g):
        for v, edge in enumerate(row):
            if edge == 1:
                edges.setdefault(u, []).append(v)

    nodes = [i for i in range(n)]

    for n in nodes:
        compute_path(explored, n, edges, topsort)

    return topsort


print(" ".join(map(str, [x+1 for x in do_topsort(graph)][::-1])))

print("DONE")
