def solve(case):
    n = int(input())
    x, y = [], []

    x = [int(a) for a in input().split(" ")]
    y = [int(b) for b in input().split(" ")]

    x.sort()
    y.sort(reverse=True)

    print(f"Case #{case}: {dot_product(x,y,n)}")


def dot_product(x, y, n):
    result = 0
    for i in range(n):
        result += x[i]*y[i]
    return result


if __name__ == "__main__":
    t = int(input())
    for c in range(t):
        solve(c+1)
        t -= 1
