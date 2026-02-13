from typing import Dict, List
from collections import defaultdict


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    t_to_ijk: Dict[int, List[List[int]]] = defaultdict()
    for l, a_l in enumerate(a):
        if a_l % 7 == 0:
            t = int(a_l / 7)
            if t not in t_to_ijk.keys():
                t_to_ijk[t] = [[l], [], []]
            else:
                t_to_ijk[t][0].append(l)

        if a_l % 5 == 0:
            t = int(a_l / 5)
            if t not in t_to_ijk.keys():
                t_to_ijk[t] = [[], [l], []]
            else:
                t_to_ijk[t][1].append(l)

        if a_l % 3 == 0:
            t = int(a_l / 3)
            if t not in t_to_ijk.keys():
                t_to_ijk[t] = [[], [], [l]]
            else:
                t_to_ijk[t][2].append(l)

    count = 0
    for t in t_to_ijk.keys():
        i_candidates = sorted(t_to_ijk[t][0])
        j_candidates = sorted(t_to_ijk[t][1])
        k_candidates = sorted(t_to_ijk[t][2])

        num_of_i_candidates = len(i_candidates)
        num_of_j_candidates = len(j_candidates)
        num_of_k_candidates = len(k_candidates)

        count += num_of_i_candidates * num_of_j_candidates * num_of_k_candidates
        for j_candidate in t_to_ijk[t][1]:
            num_of_i_less_than_j = num_of_less_than_target(i_candidates, j_candidate)

            num_of_k_more_than_j = num_of_more_than_target(k_candidates, j_candidate)

            delta0 = num_of_i_less_than_j * num_of_k_more_than_j
            num_of_i_more_than_j = num_of_more_than_target(i_candidates, j_candidate)

            num_of_k_less_than_j = num_of_less_than_target(k_candidates, j_candidate)
            delta1 = num_of_i_more_than_j * num_of_k_less_than_j

            count = count - delta0 - delta1

    print(count)


def num_of_less_than_target(candidates: List[int], target: int) -> int:
    ng = -1
    ok = len(candidates)

    while ok - ng > 1:
        mid = (ok + ng) // 2
        if candidates[mid] >= target:
            ok = mid
        else:
            ng = mid
    # 0...(ok - 1)
    return ok


def num_of_more_than_target(candidates: List[int], target: int) -> int:
    ng = -1
    ok = len(candidates)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if candidates[mid] > target:
            ok = mid
        else:
            ng = mid

    # ok...len(candidates) - 1
    return len(candidates) - ok


if __name__ == "__main__":
    main()
