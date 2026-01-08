import sys
import bisect
input = sys.stdin.readline

n, target = map(int, input().split(" "))
lst = list(map(int, input().split(" ")))

lst_idxs = [(element, i+1) for i, element in enumerate(lst)]
sortie = sorted(lst_idxs)
lst_sorted = [p for p, q in sortie]
idx_sorted = [q for p, q in sortie]

for j, num in enumerate(lst):
    search_val = target-num
    idx_val = bisect.bisect_left(lst_sorted, search_val)
    if n>idx_val>=0 and lst_sorted[idx_val] == search_val:
        if idx_sorted[idx_val] != j+1:
            print(j+1, idx_sorted[idx_val])
            sys.exit()
        else:
            if idx_val >= 1 and lst_sorted[idx_val-1] == search_val:
                print(j+1, idx_sorted[idx_val-1])
                sys.exit()


print("IMPOSSIBLE")
