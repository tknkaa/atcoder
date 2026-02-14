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
    return 0


if __name__ == "__main__":
    main()
