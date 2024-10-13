def kill_nth_person(arr, k):
    idx = 0
    while len(arr) > 1:
        idx = (idx+k-1) % len(arr)
        arr.pop(idx)
    return arr[0]


def main() -> None:
    n = 5
    k = 2
    arr = list(range(1, n + 1))
    print(kill_nth_person(arr, k))


if __name__ == '__main__':
    main()
