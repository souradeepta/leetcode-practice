def getMatchedIndexList(searchString, pattern):
    start = 0
    found = []
    length = len(pattern)
    try:
        while start < len(searchString)-1:
            indexFound = searchString.index(pattern, start)
            found.append(indexFound)
            start = indexFound + length
    except:
        raise Exception("pattern not found")
    return found


print(getMatchedIndexList("abcddabcddd", "dd"))
