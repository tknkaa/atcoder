import math


def main():
    n = int(input())
    max = int(math.sqrt(n))
    ans = []
    for i in range(1, max + 1):
        for j in range(i + 1, max + 1):
            sum = i**2 + j**2
            if sum <= n:
                ans.append(sum)

    ans.sort()
    check_list = []
    duplicates = []
    for a in ans:
        if a not in check_list:
            check_list.append(a)
        else:
            duplicates.append(a)

    ans = [a for a in ans if a not in duplicates]

    print(len(ans))
    ans_str = ""
    for a in ans:
        ans_str = ans_str + str(a) + " "
    print(ans_str.strip())


if __name__ == "__main__":
    main()
