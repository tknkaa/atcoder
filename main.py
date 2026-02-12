from typing import List
from bisect import bisect_left


def main():
    [_, q] = list(map(int, input().split(" ")))
    a_tmp = list(map(int, input().split(" ")))
    a_tmp.sort()
    inf = 10**9 + 1
    a = [-inf]
    a.extend(a_tmp)
    a.append(inf)
    answers = []
    for _ in range(0, q):
        [x, y] = list(map(int, input().split(" ")))
        ans = calc_ans(a, x, y)
        answers.append(ans)
    for answer in answers:
        print(answer)


def find_s(a: List[int], x: int) -> int:
    return bisect_left(a, x)


def find_t(a: List[int], x: int, y: int) -> int:
    s = find_s(a, x)
    ng = s - 1
    ok = len(a)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        v = (a[mid] - x + 1) - (mid - s + 1)
        if v >= y:
            ok = mid
        else:
            ng = mid

    if ok == len(a):
        return ok - 1
    else:
        return ok


def calc_ans(a: List[int], x: int, y: int) -> int:
    s = find_s(a, x)
    t = find_t(a, x, y)
    ans = x + (y - 1) + (t - s)
    return ans


if __name__ == "__main__":
    main()
