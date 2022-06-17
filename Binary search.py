def Binarysearch(a, start, last, num):
    if last>=start:
        mid = start + (last-start) // 2
        # print(mid, a[mid], end="\n")

        if a[mid] == num:
            # print("Found it!!")
            return mid
        elif a[mid] < num:
            # print(" mid is lesser")
            return(Binarysearch(a, (mid + 1), last, num))
        elif a[mid] > num:
            # print(" mid is greater")
            return(Binarysearch(a, start, mid-1, num))
    else:
        return -1
#    0    1   2   3   4   5   6    7    8    9
l = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
x = 50
ans = Binarysearch(l, 0, len(l)-1, x)
print(ans)

