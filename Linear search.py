class Linearsearch():
    def search(self, a, num):
        try:
            for i in range(0, len(a)):
                if a[i] == num:
                    return i
        except:
            return "Number not found"


LS = Linearsearch()
n = int(input("Enter the length of list/array:\t"))
l = list()
print("Enter the elements of list/array:\n")
for i in range(0, n):
    l.append(int(input("Enter the element:\t")))

num = int(input("Enter the number to search:\n"))
print(LS.search(l, num))
