import math


def main():
    n = int(input())
    max = int(math.sqrt(n))
    seen_once = set()
    duplicates = set()
    for i in range(1, max + 1):
        for j in range(i + 1, max + 1):
            sum = i**2 + j**2
            if sum <= n:
                if sum in seen_once:
                    duplicates.add(sum)
                else:
                    seen_once.add(sum)

    ans = sorted(seen_once - duplicates)

    print(len(ans))
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
