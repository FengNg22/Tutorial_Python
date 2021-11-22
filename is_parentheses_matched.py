def is_parentheses_matched(myStr):
    parentheses = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    stack_open = []
    for item in myStr:
        if item in parentheses.keys():
            stack_open.append(item)
        elif item in parentheses.values():
            if len(stack_open) > 0 and item == parentheses.get(stack_open[-1]):
                stack_open.pop()
            else:
                return "Unbalanced"
        if len(stack_open) == 0:
            return 'Balanced'


print(is_parentheses_matched('{1+[2*3]+6}'))
print(is_parentheses_matched('(1+3+(5*7])'))
print(is_parentheses_matched('(([]))'))
