global stack
stack = []

def push(i):
    stack.append(i)

def pop():
    return stack.pop(0)

def print_stack(stack):
    while (len(stack) != 0):
        print(pop())
push(1)
push(45)
push(5)
print_stack(stack)
