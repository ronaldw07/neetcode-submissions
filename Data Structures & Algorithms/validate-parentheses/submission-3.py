class Solution:
    def isValid(self, s: str) -> bool:
        

        #every open has to be closed by same type - so there has to be pairs and must track 
        #dictionary helps hold pairs
        #check most if the character is valid

        #stack becomes = [

        stack = []

        characters = {"}": "{", "]":"[", ")" : "("}

        for c in s: #for every character check if in dictionary if valid then compare to recent stack
            
            if c in characters:
                if not stack or stack[-1] != characters[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)


            
        if stack:
            return False
        else:
            return True

        


