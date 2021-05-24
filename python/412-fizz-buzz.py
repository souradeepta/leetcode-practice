class Solution:
    def fizzBuzz(self, n: int): #-> List[str]:
        if n < 1:
            return []
        output = []

        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                output.append("FizzBuzz")
            elif i % 5 == 0 and i % 3 != 0:
                output.append("Buzz")
            elif i % 5 != 0 and i % 3 == 0:
                output.append("Fizz")
            else:
                output.append(str(i))
        return output


instance = Solution()
print(instance.fizzBuzz(15))
