from heapq import heappush, heappop, heapify
import random

def generate_random_exchange_table(n=100, seed=42):
    """
    Generate a random n x n exchange rate matrix.
    - Diagonal is 1 (same currency)
    - Rates are semi-realistic with some randomness
    """
    random.seed(seed)

    # Create empty matrix
    table = [[0.0 for _ in range(n)] for _ in range(n)]

    # Fill diagonal with 1s
    for i in range(n):
        table[i][i] = 1.0

    # Fill upper triangle with random rates between 0.1 and 10
    for i in range(n):
        for j in range(i + 1, n):
            rate = random.uniform(0.1, 10.0)
            table[i][j] = rate
            # Inverse rate with small fee (0.95 to 1.05 factor)
            fee_factor = random.uniform(0.95, 1.05)
            table[j][i] = (1.0 / rate) * fee_factor

    return table


def best_exchange(frm, to, exchange_table):
    n = len(exchange_table)
    pq = []
    heapify(pq)

    best_exchange = [0 for _ in range(n)]
    best_exchange[frm] = 1

    og_set = set([frm])
    heappush(pq, (-1, frm, og_set))

    while pq:
        neg_exchange, curr_node, explored_set = pq.pop()
        neighs = exchange_table[curr_node]

        if -neg_exchange < best_exchange[curr_node]:
            continue

        for new_node, exchange_rate in enumerate(neighs):
            new_neg_exchange = exchange_rate*neg_exchange
            if new_node not in explored_set and -new_neg_exchange > best_exchange[new_node]:
                best_exchange[new_node] = -new_neg_exchange
                new_set = explored_set.copy()
                new_set.add(new_node)
                new_tuple = (new_neg_exchange, new_node, new_set)
                heappush(pq, new_tuple)

    return best_exchange[to]


if __name__ == "__main__":
    example_table = \
        [[1, 1.3, 1, 6.49],
         [0.72, 1, 0.9, 5.5],
            [1.1, 1.1, 1, 7.3],
            [0.18, 0.2, 0.136, 1]]

    val = best_exchange(1, 0, example_table)
    print(f"the best exchange value is = {val:.2f}")

    large_table = generate_random_exchange_table(n=10000, seed=42)

    # Test with large table
    print("Testing with 10000x10000 table:")
    val_large = best_exchange(0, 9999, large_table)
    print(f"Best exchange value (50x50, currency 0 to 49): {val_large:.4f}")
