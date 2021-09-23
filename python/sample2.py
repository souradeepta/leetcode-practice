from collections import Counter


def odd_ocurring_num(arr):
    count = Counter(arr)
    print(count)
    temp = 0
    total = len(count)
    for v in count.values():
        if v % 2 == 0:
            temp += v
    return total - temp




if __name__ == '__main__':
    arr = [5, 4, 8, 2, 8, 9]
    res = odd_ocurring_num(arr)
    print(res)
