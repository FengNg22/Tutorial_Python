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
            # if there has opening braces, and the close braces is == to the corresponding latest open braces
            if len(stack_open) > 0 and item == parentheses.get(stack_open[-1]):
                # remove the latest open braces since there has matched close braces
                stack_open.pop()
            else:
                return "Unbalanced"

    if len(stack_open) == 0:
        return 'Balanced'
    else:
        # for only has closed parenthesis
        return "Unbalanced"


print(is_parentheses_matched('{1+[2*3]+6}'))
print(is_parentheses_matched('(1+3+(5*7])'))
print(is_parentheses_matched('(([]))'))
print(is_parentheses_matched('3+6-3+0)'))
