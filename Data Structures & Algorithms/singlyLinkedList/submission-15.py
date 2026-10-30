class LinkedList:
    
    def __init__(self):
        self.count = 0
        self.arr = []
    
    def get(self, index: int) -> int:
        if index >= self.count:
            return -1 # non-existent value
        return self.arr[index]

    def insertHead(self, val: int) -> None:
        self.count += 1
        self.arr = [val] + self.arr
        print("insert head end")
        print("count: ", self.count, "arr: ", self.arr)

    def insertTail(self, val: int) -> None:
        self.count += 1
        self.arr = self.arr + [val]
        print("inter tail end")
        print("count: ", self.count, "arr: ", self.arr)

    def remove(self, index: int) -> bool:
        print("remove start")
        print("count: ", self.count, "arr: ", self.arr)
        if index >= self.count:
            return False
        if index == 0:
            if self.count == 1:
                self.arr = []
            else:
                self.arr = self.arr[1:]
        elif index == self.count - 1:
            if self.count == 1:
                self.arr = []
            else:
                self.arr = self.arr[:index]
        else:
            print(" I am here")
            print(self.arr[index - 1])
            print(self.arr[index + 1])
            self.arr = self.arr[:index] + self.arr[index + 1:]
        self.count -= 1
        return True

    def getValues(self) -> List[int]:
        return self.arr
        
