class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+':lambda a, b: a+b,
        '-':lambda a,b: a-b,
        '*':lambda a,b: a*b,
        '/':lambda a,b: int(a/b)}
        
        stack = []
        for i in range(len(tokens)):
            curr = tokens[i]
            if curr in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[curr](a,b))
            else:
                stack.append(int(curr))
        
        return stack[-1]
                        
                