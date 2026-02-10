from typing import List 

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
    ans: List[int] = []
    config = Config(u, v, c, l, s, t)
    state = State(1, 0, 0, ans)
    dfs(config, state)
    unique_list = set(ans)
    unique_ans = list(unique_list)
    ans_str = ""
    for ele in unique_ans:
        ans_str = ans_str + str(ele) + " "
    print(ans_str)

class Config:
    def __init__(self, u: List[int], v: List[int], c: List[int], l: int, s: int, t: int):
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


def find_neighbors_and_costs(current: int, config: Config) -> List[List[int]]:
    # [[neighbor, cost], ...]
    ans: List[List[int]] = []
    for i in range(0, len(config.u)):
        if config.u[i] == current:
            ans.append([config.v[i], config.c[i]])
    return ans

def dfs(config: Config, state: State):
    if state.total_edges < config.l:
            neighbors = find_neighbors_and_costs(state.current, config)
            for neighbor in neighbors:
                    neighbor_id = neighbor[0]
                    neighbor_cost = neighbor[1]
                    next_state = State(neighbor_id, state.total_edges + 1, state.total_cost + neighbor_cost, state.ans) 
                    dfs(config, next_state)
    elif state.total_edges == config.l and config.s <= state.total_cost <= config.t:
            state.ans.append(state.current)
            return 
    else:
            return



if __name__ == "__main__":
    main()
