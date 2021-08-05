class Stack:
    def __init__(self) :
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[self.size()-1]
    def size(self):
        return len(self.items)


a = Stack()
print("Stack is Empty: ", a.isEmpty())
a.push(1)
a.push(8)
a.push(78)
print("Push 3 element and look at stack", a.peek())
a.pop()
print("Pop last element of Stack then looking at stack", a.peek())
print("Size of Stack: ",a.size())