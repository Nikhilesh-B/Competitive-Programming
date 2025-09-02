def palindrome(s: str) -> int:
    n = len(s)
    # let's create a table, i represents the first index of the ss, j the second index these are both inclusive
    pal_ct = 0
    dp = [[0 for _ in range(n)] for _ in range(n)]
    counted_pds = set()

    for ss_len in range(1, n+1):
        for i in range(0, n-ss_len+1):
            j = i+ss_len-1
            if i == j:
                dp[i][j] = 1
                if s[i] not in counted_pds:
                    pal_ct += 1
                    counted_pds.add(s[i])
            elif j == i+1 and s[j] == s[i]:
                dp[i][j] = 1
                if s[i:j+1] not in counted_pds:
                    pal_ct += 1
                    counted_pds.add(s[i:j+1])
            elif j > i+1 and dp[i+1][j-1] and s[j] == s[i]:
                dp[i][j] = 1
                if s[i:j+1] not in counted_pds:
                    pal_ct += 1
                    counted_pds.add(s[i:j+1])

    return pal_ct


if __name__ == "__main__":
    s = "mokkori"
    ans = palindrome(s)
    print("Ans =", ans)
    s = "aabaa"
    ans = palindrome(s)
    print("Ans =", ans)
