class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        keys = {")": "(",   "}" : "{",   "]": "["}


        #starting with opening
        #since it doesnt match yet add to stack


        for c in s:
            if c in keys:
                if stack and stack[-1] == keys[c]:
                    stack.pop()
                else:
                    return False



            else:
                stack.append(c) #"([{""

        if len(stack) == 0:
            return True
        else:
            return False

