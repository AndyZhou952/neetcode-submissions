class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.tail = self.dummy
    
    def get(self, i: int) -> int:
        curr = self.dummy.next
        while curr and i > 0:
            curr = curr.next
            i -= 1
        return curr.val if curr else -1
    
    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.dummy.next)
        self.dummy.next = node

        if self.tail is self.dummy:
            self.tail = node
    
    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, i: int) -> bool:
        prev = self.dummy
        while prev.next and i > 0:
            prev = prev.next
            i -= 1
        
        if not prev.next:
            return False
        
        if prev.next is self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

    def getValues(self) -> list[int]:
        values = []
        curr = self.dummy.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values