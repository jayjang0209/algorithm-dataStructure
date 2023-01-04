def calculate(s: str):
    stack = []
    operator = "+"
    num_index = 0
    for i in range(len(s)):
        if not s[i].isnumeric() and not s[i].isspace() or i == len(s) - 1:
            if i == len(s) - 1:
                num = int(s[num_index:i+1])
            else:
                num = int(s[num_index:i])
                num_index = i + 1

            if operator == "-":
                stack.append(-num)
            elif operator == "+":
                stack.append(num)
            elif operator == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))

            operator = s[i]
    return int(sum(stack))


# s = "42"
# s = "3+2*2"
# s = "0-2147483647"
# s = " 3/2 "
# s = " 3+5 / 2 "
# s = "1-1+1"
s = "14/3*2"
print(calculate(s))