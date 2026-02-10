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
    state = State(1, 0, 0, ans)
    dfs(state, graph, l, s, t)
    unique_ans = list(set(ans))
    unique_ans.sort()
    ans_str = ""
    for ele in unique_ans:
        ans_str = ans_str + str(ele) + " "
    print(ans_str)


class Config:
    def __init__(
        self, u: List[int], v: List[int], c: List[int], l: int, s: int, t: int
    ):
        self.u = u
        self.v = v
        self.c = c
        self.l = l
        self.s = s
        self.t = t


class State:
    def __init__(self, current: int, total_edges: int, total_cost: int, ans: List[int]):
        self.current = current
        self.total_edges = total_edges
        self.total_cost = total_cost
        self.ans = ans


def dfs(state: State, graph: Dict[int, List[List[int]]], l: int, s: int, t: int):
    if state.total_edges < l:
        neighbors = graph[state.current]
        for neighbor in neighbors:
            neighbor_id = neighbor[0]
            neighbor_cost = neighbor[1]
            next_state = State(
                neighbor_id,
                state.total_edges + 1,
                state.total_cost + neighbor_cost,
                state.ans,
            )
            dfs(next_state, graph, l, s, t)
    elif state.total_edges == l and s <= state.total_cost <= t:
        state.ans.append(state.current)
        return
    else:
        return


if __name__ == "__main__":
    main()
