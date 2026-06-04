class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []


        #push 3
        #stack [3]
        #minStack [3]

        #push 4
        #stack [3,4]
        #minStack [3,3]


    def push(self, val: int) -> None:
        self.stack.append(val)

        val = min(val, self.minStack[-1] if self.minStack else val)

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        
