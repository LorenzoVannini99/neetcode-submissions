class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []
        operands = [ "+", "-", "*", "/"]
        res = 0

        for char in tokens:

            if char not in operands:
                value = int(char)
                stk.append(value)
            
            if char == "+":
                a = stk.pop()
                b = stk.pop()
                res = a + b
                stk.append(res)
            
            elif char == "-":
                a = stk.pop()
                b = stk.pop()
                res = b - a
                stk.append(res)

            elif char == "*":
                a = stk.pop()
                b = stk.pop()
                res = a * b
                stk.append(res)


            elif char == "/":
                a = stk.pop()
                b = stk.pop()
                res = int(b/a)
                stk.append(res)


        return stk[0]
        