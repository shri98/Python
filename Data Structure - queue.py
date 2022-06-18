global queue
queue = []

def push(i):
    queue.append(i)

def pop():
    return queue.pop(0)

def print_queue(queue):
    while queue:
        print(pop())

push(10)
push(32)
push(43)
push(53)
push(11)
print(pop())
push(40)
print_queue(queue)