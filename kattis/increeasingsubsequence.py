import sys
import bisect


def solve():
    for line in sys.stdin:
        numbers = list(map(int, line.strip().split()))

        if not numbers or numbers == [0]:
            break
        n = numbers[0]
        if n == 0:
            break

        lst = numbers[1:]
        deck = []
        deck_idx = []
        prev = [-1 for _ in range(n)]
        for j, num in enumerate(lst):
            i = bisect.bisect_left(deck, num)
            if i < len(deck):
                deck[i] = num
                deck_idx[i] = j
            else:
                if not deck:
                    deck.append(num)
                elif deck[-1] != num:
                    deck.append(num)
                deck_idx.append(j)

            if i > 0:
                prev[j] = deck_idx[i-1]

        ls = []
        k = deck_idx[-1] if deck_idx else -1

        while k != -1:
            ls.append(lst[k])
            k = prev[k]

        ls.reverse()

        print(len(deck), *ls)


if __name__ == "__main__":
    solve()
