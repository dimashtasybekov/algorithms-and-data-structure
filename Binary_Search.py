class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if (self.left is None):
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if (self.right is None):
                    self.right  = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def findVal(self, val):
        if val< self.data:
            if self.left is None:
                return str(val) + "Not Found from left node"
            return self.left.findVal(val)
        elif val > self.data:
            if(self.right is None):
                return str(val) + "Not Found from right node"
            return self.right.findVal(val)
        else:
            print(str(self.data)+ "found")
    def Print(self):
        if self.left:
            self.left.Print()
        print(self.data)
        if self.right:
            self.right.Print()

root = Node(10)
root.insert(2)
root.insert(5)
root.insert(99)
root.Print()
print(root.findVal(99))