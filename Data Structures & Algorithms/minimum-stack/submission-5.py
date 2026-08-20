class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []


    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append(val)
            self.minimum_stack.append(val)

        else :
            self.stack.append(val)

            if val <= self.minimum_stack[-1]:
                self.minimum_stack.append(val)


    def pop(self) -> None:
        if not self.stack:
            return 
        else :
            popped = self.stack.pop()
            if popped == self.minimum_stack[-1]:
                self.minimum_stack.pop()




    def top(self) -> int:
        if not self.stack:
            return
        else :
            return self.stack[-1]    
        

    def getMin(self) -> int:
        if not self.minimum_stack:
            return
        else:
            return self.minimum_stack[-1]    
        


        
   


