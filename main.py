from typing import List, Tuple


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    q: List[int] = []
    for a_i in a:
        q.append(a_i)
        delete_tail(q)

    print(len(q))


def delete_tail(q: List[int]) -> None:
    if len(q) < 4:
        return
    if q[len(q) - 4] == q[len(q) - 3] == q[len(q) - 2] == q[len(q) - 1]:
        for _ in range(4):
            q.pop()


if __name__ == "__main__":
    main()
