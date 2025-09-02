from collections import defaultdict

if __name__ == "__main__":
    n_m = input().split(" ")
    n = int(n_m[0])
    m = int(n_m[1])

    req_ps = [0]*m
    answers = [set() for _ in range(m)]
    n_to_p = defaultdict(set)

    ct = 0
    while n:
        k_notes = [int(x) for x in input().split(" ")]
        k = k_notes[0]
        notes = k_notes[1:]

        for note in notes:
            n_to_p[note].add(ct)
        ct += 1
        n -= 1

    note_order = [int(x) for x in input().split(" ")]

    for j, note in enumerate(note_order):
        pianos = n_to_p[note]

        if j == 0:
            if pianos:
                answers[j] = pianos
        else:
            prev_pianos = answers[j-1]
            prev_mx = req_ps[j-1]

            if prev_pianos.intersection(pianos):
                req_ps[j] = prev_mx
                answers[j] = prev_pianos.intersection(pianos)

            else:
                req_ps[j] = prev_mx+1
                answers[j] = pianos

    print(req_ps[-1])
