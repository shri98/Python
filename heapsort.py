def heapify(arr, n, root):
    largest = root
    left_node = 2*root+1
    right_node = 2*root+2

    if left_node < n and arr[left_node] > arr[largest]:
        largest = left_node

    if right_node < n and arr[right_node] > arr[largest]:
        largest = right_node

    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]

    return arr

def heap_sort(arr):

    n = len(arr)

    for i in range(n//2-1, -1,-1):
        heapify(arr, n, i)

    for i in range(n-1, 0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

l = [12, 11, 13, 5, 6, 7]
print(heap_sort(l))