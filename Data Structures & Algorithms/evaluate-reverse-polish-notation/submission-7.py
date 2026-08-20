class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []
        operands = [ "+", "-", "*", "/"]
        res = 0

        for char in tokens:

            if char not in operands:
                value = int(char)
                stk.append(value)
            
            else :
                a = stk.pop()
                b = stk.pop()       

                if char == "+":
                    res = a + b
                    stk.append(res)
                
                elif char == "-":
                    res = b - a
                    stk.append(res)

                elif char == "*":
                    res = a * b
                    stk.append(res)


                elif char == "/":
                    res = int(b / a)
                    stk.append(res)


        return stk[0]
        