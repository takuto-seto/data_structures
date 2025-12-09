class Stack:
    def __init__(self):
        # スタックのデータを保持するリスト
        self._items = []

    def is_empty(self):
        """スタックが空かどうかを返す"""
        return len(self._items) == 0

    def push(self, item):
        """データをスタックのトップに追加する"""
        # ヒント: リストの末尾に追加するメソッドを使う
        self._items.append(item)

    def pop(self):
        """スタックのトップからデータを取り出し、削除する"""
        if self.is_empty():
            return None # 空の場合は None を返す
        # ヒント: リストの末尾の要素を取り出すメソッドを使う
        return self._items.pop()
    

class Queue:
    def __init__(self):
        # キューのデータを保持するリスト
        self._items = []

    def is_empty(self):
        """キューが空かどうかを返す"""
        return len(self._items) == 0

    def enqueue(self, item):
        """データをキューの末尾に追加する"""
        # ヒント: リストの末尾に追加するメソッドを使う
        self._items.append(item)

    def dequeue(self):
        """キューの先頭からデータを取り出し、削除する"""
        if self.is_empty():
            return None
        # ヒント: リストの先頭 (インデックス 0) の要素を取り出す方法を使う
        return self._items.pop(0) # ※ pop(0) は O(N) ですが、今回は構造理解のため許容します
    

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



