def main():
    # n: cups, k: sake, x: minimum of sake
    [n, k, x] = list(map(int, input().split(" ")))
    # a_i: amount of liquid
    a = list(map(int, input().split(" ")))
    a.sort(reverse=True)
    # suppose big cups are filled with water(n - k)
    # 0, 0, 0,... ? > ? > ? ...
    for i in range(0, n - k):
        a[i] = 0
    # sum up
    sum = 0
    for i, a_i in enumerate(a):
        sum += a_i
        if sum >= x:
            print(i + 1)
            return
    print(-1)


if __name__ == "__main__":
    main()
