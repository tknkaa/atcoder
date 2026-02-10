from typing import Dict, List
from collections import defaultdict


def main():
    # n vertices, m edges
    # traverse l edges
    # the sum of the costs of the traversed edges is at least S and at most t
    [_, m, l, s, t] = list(map(int, input().split(" ")))
    # vertex u_i to v_i with cost c_i
    u = [0] * m
    v = [0] * m
    c = [0] * m
    for i in range(0, m):
        [u_i, v_i, c_i] = list(map(int, input().split(" ")))
        u[i] = u_i
        v[i] = v_i
        c[i] = c_i
    graph: defaultdict[int, List[List[int]]] = defaultdict(list)
    for i in range(0, m):
        graph[u[i]].append([v[i], c[i]])
    ans: List[int] = []
    dfs(1, 0, 0, ans, graph, l, s, t)
    unique_ans = list(set(ans))
    unique_ans.sort()
    ans_str = ""
    for ele in unique_ans:
        ans_str = ans_str + str(ele) + " "
    print(ans_str)


class State:
    def __init__(self, current: int, total_edges: int, total_cost: int, ans: List[int]):
        self.current = current
        self.total_edges = total_edges
        self.total_cost = total_cost
        self.ans = ans


def dfs(
    current: int,
    total_edges: int,
    total_cost: int,
    ans: List[int],
    graph: Dict[int, List[List[int]]],
    l: int,
    s: int,
    t: int,
):
    if total_edges < l:
        neighbors = graph[current]
        for neighbor in neighbors:
            neighbor_id = neighbor[0]
            neighbor_cost = neighbor[1]
            dfs(
                neighbor_id,
                total_edges + 1,
                total_cost + neighbor_cost,
                ans,
                graph,
                l,
                s,
                t,
            )
    elif total_edges == l and s <= total_cost <= t:
        ans.append(current)
        return
    else:
        return


if __name__ == "__main__":
    main()
