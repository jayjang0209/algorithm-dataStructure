def calculate(s: str):
    operation_map = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b)
    }
    s = s.replace(" ", "")
    tokens = []
    operators = []
    index = 0
    for i in range(len(s)):
        if not s[i].isnumeric():
            tokens.append(s[index:i])
            tokens.append(s[i])
            operators.append(s[i])
            index = i + 1
        elif i == len(s.replace(" ", "")) - 1:
            tokens.append(s[index:i + 1])
    while len(operators) != 0:
        if "*" in operators or "/" in operators:
            op = [op for op in operators if op == "*" or op == "/"].pop(0)
            print(op)
            operators.remove(op)
        else:
            op = operators.pop(0)
        op_index = tokens.index(op)
        left_operand = op_index - 1
        tokens.insert(left_operand, operation_map[tokens.pop(op_index)]
                               (int(tokens.pop(left_operand)), int(tokens.pop(left_operand))))
    return int(tokens.pop())


# s = "42"
# s = "3+2*2"
# s = "0-2147483647"
# s = " 3/2 "
# s = " 3+5 / 2 "
# s = "1-1+1"
s = "14/3*2"
print(calculate(s))