from typing import List


def string_chains(n: int, words: List[str]) -> int:

    dp = {w: 1 for w in words}
    length_dict = {len(x): [] for x in words}

    for word in words:
        length_dict[len(word)].append(word)

    lengths = list(length_dict.keys())
    lengths.sort()
    min_length = lengths[0]
    for length in lengths:
        if length > min_length:
            length_set = length_dict[length]
            for word in length_set:
                for i in range(len(word)):
                    new_word = word[0:i]+word[i+1:]
                    if new_word in dp:
                        dp[word] = max(dp[word], dp[new_word]+1)

    max_length = -1
    for x in words:
        max_length = max(max_length, dp[x])

    print("Dp", dp)
    print("Length dict", lengths)

    return max_length


if __name__ == "__main__":
    lst_words = ['a', 'and', 'bear', 'an']
    n = len(lst_words)
    ans = string_chains(n, lst_words)
    print("Answer", ans)

    lst_words = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']
    n = len(lst_words)
    ans = string_chains(n, lst_words)
    print("Answer", ans)
