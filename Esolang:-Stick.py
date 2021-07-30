# https://www.codewars.com/kata/58855acc9e1de22dff0000ef/train/python

def interpreter(tape):
    check_point = 0
    build = ""
    stack = [0,]
    idx = 0
    while idx < len(tape):
        if tape[idx] == '+':
            if stack[-1] == 255:
                stack[-1] = 0
            else:
                stack[-1] += 1
        
        elif tape[idx] == '-':
            if stack[-1] == 0:
                stack[-1] = 255
            else:
                stack[-1] -= 1
        
        elif tape[idx] == '*':
            build += chr(stack[-1])
            char_sum = 0
        
        elif tape[idx] == '^':
            stack.pop()
            char_sum -= 1
            
        elif tape[idx] == '!':
            stack.append(0)
            char_sum = 0
            
        elif tape[idx] == '[' and stack[-1] == 0:
            check_point = idx
            idx = idx+2
            continue
            
        elif tape[idx] == ']' and stack[-1] != 0:
            idx = check_point
            continue
        idx += 1
    return build[:len(stack)]


# ************************************************************************************************* #
def interpreter(tape):
    check_point, idx = 0, 0
    build, stack = "", [0,]
    while idx < len(tape):
        if tape[idx] == '+': stack[-1] = 0 if stack[-1] == 255 else stack[-1] + 1
        
        elif tape[idx] == '-': stack[-1] = 255 if stack[-1] == 0 else stack[-1] - 1
                
        elif tape[idx] == '*': build += chr(stack[-1])
        
        elif tape[idx] == '^': stack.pop()
            
        elif tape[idx] == '!': stack.append(0)
            
        elif tape[idx] == '[' and stack[-1] == 0:
            check_point = idx
            idx = idx+2
            continue
            
        elif tape[idx] == ']' and stack[-1] != 0:
            idx = check_point
            continue
        
        idx += 1
    return build[:len(stack)]
