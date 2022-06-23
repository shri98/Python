# #the number is lucky if no digit is repeated
# def is_lucky(n):
#     l = list(str(n))
#     if len(l) == len(list(set(l))):
#             return True
#     return False
#
# n = int(input("Enter the Number:\t"))
# print(is_lucky(n))


# def chocolates (arr, n) :
#     #Complete the function
#     while len(arr) > 1:
#         del arr[arr.index(max(arr))]
#
#     return arr[0]
#
# n = 5
# arr = [5, 3, 1, 6, 9]
#
# print(chocolates(arr, n))

## Rotate array twice

arr = [1, 2, 3, 4, 5]
q = []
n = input("Number of times to rotate array: -\n")
for i in range(int(n) % len(arr)):
    q.append(arr.pop(-1))
while arr:
    q.append(arr.pop(0))

    # print(arr)

print(q)