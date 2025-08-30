def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0
def infix_to_postfix(expression):
    stack = []
    result = ''
    for char in expression:
        if char.isalnum():
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and precedence(char)<=precedence((stack[-1])):
             result+=stack.pop()
            stack.append(char)
        while stack:
         result += stack.pop()
    return result
# Example
print(infix_to_postfix("a+b*(c-d)"))