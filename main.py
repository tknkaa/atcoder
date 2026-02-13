from typing import List, Tuple


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    found = True
    while found:
        a, found = find_and_delete_4(a)
    print(len(a))


def find_and_delete_4(a: List[int]) -> Tuple[List[int], bool]:
    if len(a) < 4:
        return (a, False)
    for i in range(0, len(a) - 3):
        if a[i] == a[i + 1] == a[i + 2] == a[i + 3]:
            return (a[: max([i, 0])] + a[(i + 4) :], True)
    return (a, False)


if __name__ == "__main__":
    main()
