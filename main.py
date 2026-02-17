from typing import List


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 998244353
    a.sort()

    # Prefix sum: prefix[i] = sum of a[0..i-1]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    result = 0
    for j in range(m):
        x = find_x(b[j], a)
        result += (b[j] * x - prefix[x]) % c
        result += ((prefix[n] - prefix[x]) - b[j] * (n - x)) % c
    result %= c
    print(result)


def find_x(b_j: int, a: List[int]) -> int:
    ng = -1
    ok = len(a)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if a[mid] >= b_j:
            ok = mid
        else:
            ng = mid
    return ok


if __name__ == "__main__":
    main()
