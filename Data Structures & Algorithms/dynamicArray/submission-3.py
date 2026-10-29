class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capcity must be greater than 0")
        self.array = [0] * capacity
        self.used = 0
        self.total = capacity

    def get(self, i: int) -> int:
        if i >= self.total:
            raise ValueError("The index provided is not available")
        elif i < 0:
            raise ValueError("The index must be non-negative")
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.total:
            raise ValueError("The index provided is not available")
        elif i < 0:
            raise ValueError("The index must be non-negative")
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.total == self.used:
            self.resize()
        self.array[self.used] = n
        self.used += 1

    def popback(self) -> int:
        if self.used == 0:
            raise IndexError("no value to pop")
        popped = self.array[self.used - 1]
        self.array[self.used - 1] = 0
        self.used -= 1
        return popped

    def resize(self) -> None:
        new_array = [0] * 2 * self.total
        for i in range(self.total):
            new_array[i] = self.array[i]
        self.array = new_array
        self.total *= 2

    def getSize(self) -> int:
        return self.used
    
    def getCapacity(self) -> int:
        return self.total
