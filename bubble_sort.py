def bubble_sort(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if a[j] >= a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

l = [5, 1, 4, 2, 8]
print(bubble_sort(l))