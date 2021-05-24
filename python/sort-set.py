from typing import List


def sort_set(input: List) -> List:
    l = 0
    r = len(input) - 1
    while l < r:
        # if input[l] == 0:
        #     idx = l
        # if input[r] == 0:
        #     idx = r

        if input[l] > 0 and input[r] < 0:
            input[l], input[r] = input[r], input[l]
            r -= 1
            l += 1
        elif input[l] > 0:
            r -= 1
        elif input[l] == 0:
            idx = l
        else:
            l += 1

    return input


def main():
    input = [3, 1, -5, -2, 6, 0]
    result = sort_set(input)
    print(result)


if __name__ == '__main__':
    main()
