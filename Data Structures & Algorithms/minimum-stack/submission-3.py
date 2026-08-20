class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk :
            self.stk.append([val,val])
        else :
            minimum = min ( val , self.stk[-1][1])
            self.stk.append( [val, minimum] )

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]


    def getMin(self) -> int:
        return self.stk[-1][1]


