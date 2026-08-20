class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append([val, val])
        else:
            current_min = min(val, self.stk[-1][1])
            self.stk.append([val, current_min])

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]

