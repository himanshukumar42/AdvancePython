import math


def hourly_eating(piles, hourly):
    total_hours= 0
    for i in range(len(piles)):
        total_hours += math.ceil(piles[i] / hourly)
    return total_hours


def koko_eating_bananas(piles, h):
    low, high = 1, max(piles)
    ans = None
    while low <= high:
        mid = (low + high) // 2
        total_hours = hourly_eating(piles, mid)
        if total_hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def main() -> None:
    piles = [3, 6, 7, 11]
    h = 8
    print(koko_eating_bananas(piles, h))


if __name__ == '__main__':
    main()
