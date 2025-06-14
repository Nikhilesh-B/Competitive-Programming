def keep_going(transition_types):
    rval = False
    for i in range(1, 7):
        rval = rval or transition_types[i]
    return rval


def marble_game(m1, m2, m3):
    n1 = len(m1)
    n2 = len(m2)
    n3 = len(m3)
    transition_types = {i: 0 for i in range(1, 7)}

    for marble_group in [m1, m2, m3]:
        for marble in marble_group:
            if marble_group == m1:
                # 1->2
                if n2+n1+1 > marble > n1:
                    transition_types[1] += 1
                # 1->3
                elif marble > n2+n1:
                    transition_types[2] += 1
            elif marble_group == m2:
                # 2->1
                if n1+1 > marble:
                    transition_types[3] += 1
                # 2->3
                elif marble > n2+n1:
                    transition_types[4] += 1
            else:
                # 3->1
                if n1+1 > marble:
                    transition_types[5] += 1
                # 3->2
                elif n2+n1+1 > marble > n1:
                    transition_types[6] += 1

    count = 0

    while keep_going(transition_types):
        if transition_types[1] and transition_types[3] and transition_types[5]:
            count += 2
            for j in [1, 3, 5]:
                transition_types[j] -= 1

        elif transition_types[2] and transition_types[4] and transition_types[6]:
            count += 2
            for j in [2, 4, 6]:
                transition_types[j] -= 1

        elif transition_types[1] and transition_types[3]:
            count += 1
            for j in [1, 3]:
                transition_types[j] -= 1

        elif transition_types[2] and transition_types[5]:
            count += 1
            for j in [2, 5]:
                transition_types[j] -= 1

        elif transition_types[4] and transition_types[6]:
            count += 1
            for j in [4, 6]:
                transition_types[j] -= 1
    return count


if __name__ == "__main__":
    m1 = [2]
    m2 = [1, 6, 4]
    m3 = [3, 5]
    sol = marble_game(m1, m2, m3)
    print("Optimal solution", sol)
