class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        return True

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(len(self.items) - 1)      

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            self.items = self.items[0:self.limit]
            return True
        else:
            return False

    def search(self, target):
        pass
        # reversed_items = []
        # if target not in self.items:
        #     return -1
        # else:
        #     while self.items:
        #         for item in self.items:
        #             i = len(self.items) - 1
        #             self.items.pop(i)
        #             reversed_items.insert(0, item)
        #     return reversed_items.index(target)
            # self.items.reverse()
            # return self.items.index(target)


# drivers = [33,45,16,55,62,10]
# drivers.reverse()
# print(drivers.index(55))