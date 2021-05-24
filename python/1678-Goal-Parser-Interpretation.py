class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        set = 0
        if not command:
            return result

        for i in range(len(command)):
            if command[i] == '(':
                set = i
            elif command[i] == ')':
                if set+1 == i:
                    result += 'o'
                else:
                    continue
            else:
                result += command[i]

        return result


s = Solution()

assert "Goal" == s.interpret("G()(al)"), "incorrect result"
assert "Gooooal" == s.interpret("G()()()()(al)"), "incorrect result"
assert "alGalooG" == s.interpret("(al)G(al)()()G"), "incorrect result"
