from collections import deque
class Stack():
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0
    
    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self._items[-1]
    
    
    

    

# class Queue():
#     def __init__(self):
#         self._items = []

#     def is_empty(self):
#         return len(self._items) == 0
    
#     def enqueue(self, item):
#         self._items.append(item)

#     def dequeue(self):
#         if self.is_empty():
#             return None
        
#         return self._items.pop(0)
    
#     def peek(self):
#         if self.is_empty():
#             return None
        
#         return self._items[-1]
    

class EfficientQueue():
    def __init__(self):
        self._items = deque()

    def is_empty(self):
        return len(self._items) == 0
    
    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        
        return self._items.popleft()
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self._items[0]   


    

if __name__ == '__main__':
    
    # --- スタックのテスト ---
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    # LIFO: 30が最初に出るべき
    assert stack.pop() == 30, "スタックテスト失敗: LIFO違反"
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.pop() == None, "スタックテスト失敗: 空のポップ"
    print("✅ スタックのテストが成功しました。")

    # --- キューのテスト ---
    queue = Queue()
    assert queue.is_empty() == True
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    # FIFO: Aが最初に出るべき
    assert queue.dequeue() == "A", "キューテスト失敗: FIFO違反"
    assert queue.dequeue() == "B"
    assert queue.dequeue() == "C"
    assert queue.dequeue() == None, "キューテスト失敗: 空のデキュー"
    print("✅ キューのテストが成功しました。")



