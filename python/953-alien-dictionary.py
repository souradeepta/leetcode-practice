class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        length = len(order)
        indexed = {}
        for i in range(length):
            elem = order[i]
            indexed[elem] = i
        
      #  print(indexed)
        for i in range(len(words)- 1):
            word1 = words[i]
            word2 = words[i+ 1]
            
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if indexed[word1[j]] > indexed[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        
        return True


instance = Solution()
result = instance.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
result2 = instance.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
results = []
results.append(result)
results.append(result2)
print(results)