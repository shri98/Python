def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        num = l[i]
        while j >= 0 and num < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = num

    return l
#    0   1   2   3  4
l = [12, 11, 13, 5, 6]
print(insertion_sort(l))