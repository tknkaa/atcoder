from typing import Set, List


def main():
    [_, m] = list(map(int, input().split()))
    blocks: Set[tuple] = set()
    count = 0

    for _ in range(0, m):
        [r, c] = list(map(int, input().split()))
        ok = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (r + i, c + j) in blocks:
                    ok = False
        if ok:
            blocks.add((r, c))
            count += 1
    print(count)


if __name__ == "__main__":
    main()
