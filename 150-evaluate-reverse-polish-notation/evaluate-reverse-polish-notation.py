class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    opr2 = int(stack.pop())
                    opr1 = int(stack.pop())
                    stack.append((opr1) + (opr2))
                case '-':
                    opr2 = int(stack.pop())
                    opr1 = int(stack.pop())
                    stack.append((opr1) - (opr2))
                    print(f"{opr1} - {opr2}")
                    print((opr1) - (opr2))
                case '*':
                    opr2 = int(stack.pop())
                    opr1 = int(stack.pop())
                    stack.append((opr1) * (opr2))
                case '/':
                    opr2 = int(stack.pop())
                    opr1 = int(stack.pop())
                    if opr1 / opr2 < 0 and opr1 % opr2 != 0:
                        stack.append((opr1) // (opr2) + 1)
                    else:
                        stack.append((opr1) // (opr2))
                case _:
                    stack.append(token)

        return int(stack[0])
                