from typing import List, Tuple


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    indexed = [(i, e) for (i, e) in enumerate(a)]
    ordered = sorted(indexed, key=lambda x: x[1])
    count = 0
    answers: List[List[Tuple[int, int]]] = []
    for k_new, k in enumerate(ordered):
        v = k[1]
        if v % 3 == 0:
            if k_new + 1 >= len(ordered):
                continue
            remain = ordered[(k_new + 1) :]
            target = int(v / 3 * 5)
            founds = bin_search(remain, target)
            if len(founds) == 0:
                continue
            else:
                for found in founds:
                    j_new = found + k_new + 1
                    j = ordered[j_new]
                    if j_new + 1 >= len(ordered):
                        break
                    remain = ordered[(j_new + 1) :]
                    target = int(v / 3 * 7)
                    founds = bin_search(remain, target)
                    if len(founds) == 0:
                        break
                    else:
                        for found in founds:
                            i_new = found + j_new + 1
                            i = ordered[i_new]
                            k_idx = k[0]
                            j_idx = j[0]
                            i_idx = i[0]
                            if (
                                min([k_idx, j_idx, i_idx]) == j_idx
                                or max([k_idx, j_idx, i_idx]) == j_idx
                            ):
                                count += 1
                                answers.append([k, j, i])
        else:
            continue
    print(count)
    # print(answers)


def bin_search(remain: List[Tuple[int, int]], target: int) -> List[int]:
    ng = -1
    ok = len(remain)
    ans = []
    while ok - ng > 1:
        mid = (ng + ok) // 2
        if remain[mid][1] >= target:
            ok = mid
        else:
            ng = mid
    if ok >= len(remain) or remain[ok][1] != target:
        return ans
    while ok <= len(remain) - 1 and remain[ok][1] == target:
        ans.append(ok)
        ok += 1
    return ans


if __name__ == "__main__":
    main()
