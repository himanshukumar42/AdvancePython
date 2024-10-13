def main():
    arr = [1, 2, 4, 2, 4, 2, 2, 5]
    count_duplicates = lambda arr: {a: arr.count(a) for a in set(arr)}
    print(count_duplicates(arr))


if __name__ == '__main__':
    main()
