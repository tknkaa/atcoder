def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort(reverse=True)
    alice = 0
    bob = 0
    for i in range(0, n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    print(alice - bob)


if __name__ == "__main__":
    main()
