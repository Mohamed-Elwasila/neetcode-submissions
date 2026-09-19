class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":    
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                i = stack.pop()
                j = stack.pop()
                stack.append(j - i)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                i = stack.pop()
                j = stack.pop()
                stack.append(int(j / i))
            else:
                stack.append(int(t))
            
        return stack[0]