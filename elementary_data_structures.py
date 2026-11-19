
from collections import deque


# 1. ARRAY
class MyArray:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def delete(self, value):
        if value in self.items:
            self.items.remove(value)

    def access(self, index):
        return self.items[index]

    def display(self):
        return self.items


# 2. MATRIX
class Matrix:
    def __init__(self, rows, columns):
        self.data = [
            [0 for _ in range(columns)]
            for _ in range(rows)
        ]

    def insert(self, row, column, value):
        self.data[row][column] = value

    def access(self, row, column):
        return self.data[row][column]

    def delete(self, row, column):
        self.data[row][column] = 0

    def display(self):
        return self.data


# 3. STACK (using an array)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def display(self):
        return self.items


# 4. QUEUE (using an array)
class Queue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.front >= len(self.items):
            return None

        value = self.items[self.front]
        self.front += 1

        # Occasionally remove unused space
        if self.front > 50 and self.front * 2 >= len(self.items):
            self.items = self.items[self.front:]
            self.front = 0

        return value

    def display(self):
        return self.items[self.front:]


# 5. SINGLY LINKED LIST
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next

        return values


# TEST ALL DATA STRUCTURES
if __name__ == "__main__":

    print("ARRAY")
    arr = MyArray()
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)
    print("Original:", arr.display())
    print("Access index 1:", arr.access(1))
    arr.delete(20)
    print("After deletion:", arr.display())

    print("\nMATRIX")
    matrix = Matrix(2, 2)
    matrix.insert(0, 0, 5)
    matrix.insert(1, 1, 10)
    print("Original:", matrix.display())
    print("Access (1,1):", matrix.access(1, 1))
    matrix.delete(0, 0)
    print("After deletion:", matrix.display())

    print("\nSTACK")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Original:", stack.display())
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())
    print("After pop:", stack.display())

    print("\nQUEUE")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Original:", queue.display())
    print("Dequeue:", queue.dequeue())
    print("After dequeue:", queue.display())

    print("\nLINKED LIST")
    linked = LinkedList()
    linked.insert(10)
    linked.insert(20)
    linked.insert(30)
    print("Original:", linked.display())
    linked.delete(20)
    print("After deletion:", linked.display())
