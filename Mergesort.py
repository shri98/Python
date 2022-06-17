def mergesort(a):
    if len(a) > 1:
        mid = len(a)//2

        L = a[:mid]
        R = a[mid:]

        mergesort(L)
        mergesort(R)

        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i+=1
                k+=1
            else:
                a[k] = R[j]
                j+=1
                k+=1

    return a


l = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(l))