# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        countDict = {}
        for i in range(len(J)):
            countDict[J[i]] = 0
        
        for j in range(len(S)):
            if S[j] in countDict.keys():
                countDict[S[j]] += 1
        print(countDict)
               
        sum = 0
        for value in countDict.values():
            sum += value
            
        return sum