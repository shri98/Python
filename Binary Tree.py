##Important Note:- Please do check if you return from function while inserting

class node:

    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def getroot(self):
        return self.root

    def insert(self, value):

        if not self.root:
            self.root = node(value)
            return

        q = [self.root]
        while q:
            temp = q.pop(0)
            if not temp.left:

                temp.left = node(value)

                return
            else:

                q.append(temp.left)

            if not temp.right:

                temp.right = node(value)

                return
            else:

                q.append(temp.right)

    def display(self, root):
        if root:
            # print("root value:- ", root.key)
            self.display(root.left)
            print(root.key)
            self.display(root.right)


t = Tree()

t.insert(10)
t.insert(11)
t.insert(7)
t.insert(9)
t.insert(15)
t.insert(8)
t.insert(20)
t.display(t.getroot())
