class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = []
        for token in tokens:        
            if token == "+":
                first = exp.pop()
                second = exp.pop()
                exp.append(first + second)
            elif token == '-':
                first = exp.pop()
                second = exp.pop()
                exp.append(second - first)
            elif token == '*':
                first = exp.pop()
                second = exp.pop()
                exp.append(first * second)
            elif token == '/':
                first = exp.pop()
                second = exp.pop()
                exp.append(int(second / first))
            else:
                exp.append(int(token))
        return exp[0]