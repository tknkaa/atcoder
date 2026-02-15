from typing import List


def main():
    t = int(input())
    answers: List[int] = []
    for _ in range(0, t):
        n = int(input())
        w: List[int] = []
        p: List[int] = []
        for _ in range(0, n):
            [w_i, p_i] = list(map(int, input().split()))
            w.append(w_i)
            p.append(p_i)
        answer = solve(w, p)
        answers.append(answer)

    for answer in answers:
        print(answer)


def solve(w: List[int], p: List[int]) -> int:
    sum_p = sum(p)
    w_plus_p = [w[i] + p[i] for i in range(0, len(w))]
    w_plus_p.sort()
    sum_w_plus_p = 0
    num_of_deer = 0
    while sum_w_plus_p <= sum_p:
        sum_w_plus_p += w_plus_p[num_of_deer]
        num_of_deer += 1
    return num_of_deer - 1


if __name__ == "__main__":
    main()
