class Queue:
    def __init__(self):
        self.queue = list()
    def addtoq(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False

    def size(self):
        return len(self.queue)
    
    def remove(self):
        if(len(self.queue)>0):
            return self.queue.pop()
        return ("No elements in Queue")



Q = Queue()
Q.addtoq("1")
Q.addtoq(2)
Q.addtoq(3)
print(Q.size())
Q.remove()
print(Q.size())