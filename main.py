def main():
    n = int(input())
    c = [0] * (n + 1)
    x = 1
    while x**2 <= n:
        y = x + 1
        while x**2 + y**2 <= n:
            c[x**2 + y**2] += 1
            y += 1
        x += 1
    ans = [i for i in range(1, len(c)) if c[i] == 1]
    print(len(ans))
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
