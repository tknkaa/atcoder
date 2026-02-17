from collections import defaultdict, deque
from typing import Dict, Tuple, List, Set, Optional


def main():
    [h, w] = list(map(int, input().split()))
    field: List[List[str]] = [["" for _ in range(w)] for _ in range(h)]
    for i in range(0, h):
        s = input()
        for j in range(0, w):
            field[i][j] = s[j]
    warp: Dict[str, Set[Tuple[int, int]]] = defaultdict(set)
    for i in range(0, h):
        for j in range(0, w):
            ch = field[i][j]
            if ch.isalpha() and ch.islower():
                warp[ch].add((i, j))
    start_position: Tuple[int, int] = (0, 0)
    result = process(start_position, field, h, w, warp)
    print(result)


def process(
    start: Tuple[int, int],
    field: List[List[str]],
    h: int,
    w: int,
    warp: Dict[str, Set[Tuple[int, int]]],
) -> int:
    goal = (h - 1, w - 1)
    if start == goal:
        return 0
    visited: Set[Tuple[int, int]] = {start}
    used_warps: Set[str] = set()
    queue: deque = deque([(start, 0, used_warps)])
    while queue:
        current_position, count, used_warps = queue.popleft()
        possible_positions = find_possible_next_positions(
            current_position, field, h, w, warp, used_warps
        )
        for position in possible_positions:
            if position in visited:
                continue
            if position == goal:
                return count + 1
            visited.add(position)
            new_used_warps = used_warps.copy()
            ch = field[current_position[0]][current_position[1]]
            if ch.isalpha() and ch.islower():
                new_used_warps.add(ch)
            queue.append((position, count + 1, new_used_warps))
    return -1


def find_possible_next_positions(
    current_position: Tuple[int, int],
    field: List[List[str]],
    h: int,
    w: int,
    warp: Dict[str, Set[Tuple[int, int]]],
    used_warps: Optional[Set[str]] = None,
) -> Set[Tuple[int, int]]:
    if used_warps is None:
        used_warps = set()
    i = current_position[0]
    j = current_position[1]
    valid_neighbors = find_valid_neighbors(current_position, field, h, w)
    if field[i][j] == ".":
        return valid_neighbors
    else:
        ch = field[i][j]
        if ch in used_warps:
            return valid_neighbors
        warp_dests = warp[ch]
        return valid_neighbors.union(warp_dests)


def find_valid_neighbors(
    current_position: Tuple[int, int], field: List[List[str]], h: int, w: int
) -> Set[Tuple[int, int]]:
    valid_neighbors: Set[Tuple[int, int]] = set()
    i = current_position[0]
    j = current_position[1]
    if i - 1 >= 0 and j - 1 >= 0 and field[i - 1][j - 1] != "#":
        valid_neighbors.add((i - 1, j - 1))
    if j - 1 >= 0 and field[i][j - 1] != "#":
        valid_neighbors.add((i, j - 1))
    if i + 1 <= h - 1 and j - 1 >= 0 and field[i + 1][j - 1] != "#":
        valid_neighbors.add((i + 1, j - 1))
    if i - 1 >= 0 and field[i - 1][j] != "#":
        valid_neighbors.add((i - 1, j))
    if i - 1 >= 0 and j + 1 <= w - 1 and field[i - 1][j + 1] != "#":
        valid_neighbors.add((i - 1, j + 1))
    if j + 1 <= w - 1 and field[i][j + 1] != "#":
        valid_neighbors.add((i, j + 1))
    if i + 1 <= h - 1 and field[i + 1][j] != "#":
        valid_neighbors.add((i + 1, j))
    if i + 1 <= h - 1 and j + 1 <= w - 1 and field[i + 1][j + 1] != "#":
        valid_neighbors.add((i + 1, j + 1))
    return valid_neighbors


if __name__ == "__main__":
    main()
