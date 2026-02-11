from typing import List


def main():
    t = int(input())
    min_costs = [0] * t
    for i in range(0, t):
        [n, w] = list(map(int, input().split(" ")))
        c = list(map(int, input().split(" ")))
        min_costs[i] = min_cost(n, w, c)
    for cost in min_costs:
        print(cost)


def min_cost(n: int, w: int, c: List[int]) -> int:
    circle = [0] * (2 * w)
    cycles = int(n / (2 * w))
    for x in range(0, 2 * w):
        for i in range(0, cycles + 1):
            if x + i * 2 * w >= n:
                continue
            else:
                circle[x] += c[x + i * 2 * w]
    circle = circle * 3
    sums = [0] * (2 * w)

    current_sum = sum(circle[0:w])
    for start in range(0, 2 * w):
        current_sum = current_sum - circle[start] + circle[start + w]
        sums[start] = current_sum
    return min(sums)


if __name__ == "__main__":
    main()
