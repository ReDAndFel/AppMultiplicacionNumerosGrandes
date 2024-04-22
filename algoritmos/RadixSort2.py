#Algoritmos sacado del classroom

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        self.size += 1
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        self.size -= 1
        temp = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp

    def is_empty(self):
        return self.size == 0

class RadixSort:
    def __init__(self):
        self.queues = [LinkedQueue() for _ in range(10)]

    def sort(self, arr):
        max_num = max(arr)
        num_digits = len(str(max_num))

        for i in range(1, num_digits + 1):
            for num in arr:
                self.queues[self.get_digit(num, i)].enqueue(num)

            pos = 0
            for j in range(10):
                while not self.queues[j].is_empty():
                    arr[pos] = self.queues[j].dequeue()
                    pos += 1

    def get_digit(self, num, d):
        return (num // 10 ** (d - 1)) % 10

def radixSort2(arr):
    radix_sort = RadixSort()
    radix_sort.sort(arr)
    return arr