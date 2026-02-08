def main():
    n = int(input())
    # initial state
    t = [0]
    x = [0]
    y = [0]
    for _ in range(0, n):
        [a, b, c] = list(map(int, input().split(" ")))
        t.append(a)
        x.append(b)
        y.append(c)

    # length of states should be n + 1
    for i in range(0, n):
        x0 = x[i]
        x1 = x[i + 1]
        y0 = y[i]
        y1 = y[i + 1]
        t0 = t[i]
        t1 = t[i + 1]
        if judge(t0, t1, dist(x0, x1, y0, y1)):
            continue
        else:
            print("No")
            return
    print("Yes")


def dist(x0, x1, y0, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def judge(t0, t1, dist):
    lag = t1 - t0
    if lag - dist >= 0 and (lag - dist) % 2 == 0:
        return True
    return False


if __name__ == "__main__":
    main()
