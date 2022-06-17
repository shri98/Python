def selection_sort(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]> a[j]:
                a[i],a[j] = a[j],a[i]

    return a
A = [64, 25, 12, 22, 11]
print(selection_sort(A))
