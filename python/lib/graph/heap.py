class heap:
    
    def __init__(self):
        self.heap = []
    
    def push(self, x):
        self.heap.append(x)  # 最後尾に挿入
        i = len(self.heap) - 1  # 挿入された頂点番号
        while i > 0:
            p = (i - 1) // 2  # 親の頂点番号
            if self.heap[p] >= x:
                break  # 逆転がなければ終了
            self.heap[i] = self.heap[p]  # 自分の値が大きければ親と変わる
            i = p
        self.heap[i] = x

    def top(self):
        if self.heap == []:
            return -1
        return self.heap[0]

    def pop(self):
        if self.heap == []:
            return
        x = self.heap.pop()
        i = 0
        while i * 2 + 1 < len(self.heap):
            child1 = i * 2 + 1
            child2 = i * 2 + 2
            if child2 < len(self.heap) and self.heap[child2] > self.heap[child1]:
                child1 = child2
            if self.heap[child1] <= x:
                break
            self.heap[i] = self.heap[child1]
            i = child1
        self.heap[i] = x


def main():
    # numbers = list(map(int, input().split()))
    _heap = heap()
    # for num in numbers:  # O(NlogN)
    #     _heap.push(num)
    _heap.push(5)
    _heap.push(3)
    _heap.push(7)
    _heap.push(1)
    print(_heap.top())
    _heap.pop()
    print(_heap.top())
    _heap.push(11)
    print(_heap.top())

    print(_heap.heap)


if __name__ == "__main__":
    main()
