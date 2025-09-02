def manual_count_palindromes(s):
    """Manually count unique palindromes for verification"""
    unique_pals = set()
    n = len(s)

    # Check all possible substrings
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1]:  # Check if palindrome
                unique_pals.add(substring)

    return len(unique_pals), sorted(unique_pals)


# Test cases
test_cases = ["mokkori", "aabaa"]

for s in test_cases:
    count, palindromes = manual_count_palindromes(s)
    print(f"String: '{s}'")
    print(f"Manual count: {count}")
    print(f"Unique palindromes: {palindromes}")
    print()
