# #the number is lucky if no digit is repeated
# def is_lucky(n):
#     l = list(str(n))
#     if len(l) == len(list(set(l))):
#             return True
#     return False
#
# n = int(input("Enter the Number:\t"))
# print(is_lucky(n))


def chocolates (arr, n) :
    #Complete the function
    while len(arr) > 1:
        del arr[arr.index(max(arr))]

    return arr[0]

n = 5
arr = [5, 3, 1, 6, 9]

print(chocolates(arr, n))