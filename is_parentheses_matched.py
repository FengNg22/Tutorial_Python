def is_parentheses_matched(myStr):
    parentheses = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    stack_open = []
    parentheses_exist= False
    for item in myStr:
        if item in parentheses.keys():
            parentheses_exist= True
            stack_open.append(item)
        elif item in parentheses.values():
            parentheses_exist = True
            # if there has opening braces, and the close braces is == to the corresponding latest open braces
            if len(stack_open) > 0 and item == parentheses.get(stack_open[-1]):
                # remove the latest open braces since there has matched close braces
                stack_open.pop()
            else:
                return "Unbalancedd"


    if len(stack_open) == 0:
        if parentheses_exist:
                return 'Balanced'
        else:
            return " No Parenthesis Exist"
    else:
        # for only has open parenthesis
        return "Unbalanced"



print(is_parentheses_matched('{1+[2*3]+6}'))
print(is_parentheses_matched('(1+3+(5*7])'))
print(is_parentheses_matched('(([]))'))
print(is_parentheses_matched('3+6-3+0)'))
