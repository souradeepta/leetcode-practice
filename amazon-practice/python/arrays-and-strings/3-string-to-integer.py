# String to integer (atoi)
# Brute force:: Time:

class Solution:
    def myAtoi(self, str: str) -> int:
        
        intMax = (2**31) - 1    #2147483647
        intMin = -(2**31) #-2147483647

        str = str.strip() #remove white spaces

        # check if input is only spaces
        if not str:
            return 0

        sign = 1
        i = 0

        if str[i] == "+":
            i = i + 1
        elif str[i] == "-":
            i = i + 1
            sign = -1

        num = 0

        while i < len(str):
            if not str[i].isdigit():
                break
            
            num = num*10 + ord(str[i]) - ord('0')

            if num > intMax:
                break
            i = i + 1

        result =  min(max(sign * num, intMin), intMax)
        return result