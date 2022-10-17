# Python 3rd, stack based O(n) solution
# The idea behind this is:
# If the number is positive, if we have a sequence of numbers going left to right where the number after 5 is greater than 5, we remove that 5. Otherwise, remove the 5 from the last.
# If the number is negative, if we have a sequence of numbers going left to right where the number after 5 is less than 5, we remove that 5. Otherwise, remove the 5 from the last.

def solution(A):
    if(A>=0):
        return case(A)
    return -1*case(A)

def case(A):
    strA = str(A)
    stack = []
    if(A<0):
        strA = strA[1:]
    removedFiveFlag = False
    for char in strA:
        num = int(char)
        if((not removedFiveFlag) and len(stack)!=0 and stack[-1]==5 and ((A<0 and num<5) or (A>0 and num>5))):
            stack.pop()
            stack.append(num)
            removedFiveFlag = True
        else:
            stack.append(num)
    fiveIndex = -1
    if(not removedFiveFlag):
        for i in range(len(stack)-1, -1, -1):
            if(stack[i]==5):
                fiveIndex = i
                break
        stack.pop(fiveIndex)
    return buildResult(stack)

def buildResult(stack):
    result = 0
    for num in stack:
        result = result * 10 + num
    return result

print(solution(-15625))
print(solution(-15425))
print(solution(-154535))
print(solution(15958))