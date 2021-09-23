def countGroups(related):
    # Write your code here
    count = 0
    length = len(related)
    related = convertToArray(related)

    for indx in range(length):
        if related[indx][indx] == 1:
            count += 1
            dfs(indx, length, related)
    return count


def dfs(idx, length, matrix):
    if matrix[idx][idx] == 0:
        return
    for i in range(length):
        if matrix[idx][i] == 1:
            matrix[idx][i] = 0
            dfs(i, length, matrix)


def convertToArray(s):
    result = []
    for char in s:
        result.append([int(x) for x in char])
    return result


related = ["1100", "1110", "0110", "0001"]
ans = countGroups(related)
print(ans)