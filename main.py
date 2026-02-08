def main():
    s = int(input())
    s1 = int(s / 100)
    s2 = int(s / 10 - s1 * 10)
    s3 = int(s - s1 * 100 - s2 * 10)
    print(s1 + s2 + s3)


if __name__ == "__main__":
    main()
