def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d1 = [0] * n
    d2 = [0] * n
    d3 = [0] * n
    for i in range(0, n):
        if i == 0:
            d1[i] = a[i]
        else:
            d1[i] = d1[i - 1] + a[i]
    for i in range(1, n):
        d2[i] = max([d1[i - 1], d2[i - 1]]) + b[i]
    for i in range(2, n):
        d3[i] = max([d2[i - 1], d3[i - 1]]) + c[i]
    print(d3[n - 1])


if __name__ == "__main__":
    main()
