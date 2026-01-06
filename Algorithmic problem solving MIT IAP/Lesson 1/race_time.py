import sys
input = sys.stdin.readline

N, K = list(map(int, input().split(" ")))
S_D = []

for _ in range(N):
    s_d = tuple(map(int, input().split(" ")))
    S_D.append(s_d)


def f(t):
    p_t = [s*t+d for s, d in S_D]
    return max(p_t)-min(p_t)


lo_t, hi_t = 0, K

lft_ptr, rht_ptr = lo_t+(hi_t-lo_t)/3, lo_t+2*(hi_t-lo_t)/3


while hi_t-lo_t > 1e-9:
    lft_ptr, rht_ptr = lo_t+(hi_t-lo_t)/3, lo_t+2*(hi_t-lo_t)/3
    l_val, r_val = f(lft_ptr), f(rht_ptr)
    if l_val < r_val:
        hi_t = rht_ptr
    else:
        lo_t = lft_ptr


print(f"{f(lo_t):.6f}")
