graph = [[0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1],
         [1, 0, 0, 0]]

# three states unvisted, explored, visited <= viisted means done, explored means ur expanding from that graph
n = len(graph)

states = [0 for _ in range(n)]
parents = [-1 for _ in range(n)]
edges = {}
cycle = False

for u, row in enumerate(graph):
    for v, e in enumerate(row):
        if e:
            edges.setdefault(u, []).append(v)


def cyclecheck(v):
    states[v] = 1
    global cycle
    if cycle:
        return

    if v in edges:
        for chd in edges[v]:
            if states[chd] == 0:
                parents[chd] = v
                cyclecheck(chd)
            elif states[chd] == 1:
                if (chd == parents[v]):
                    print("TRIVIAL CYCLE RIGHT HERE")
                else:
                    cycle = True
                    print("CYCLE DETECTED")
                    return

            else:
                print("CROSS EDGE")

    states[v] = 2


for i in range(n):
    cyclecheck(i)

if cycle:
    print(-1)
else:
    print(0)
