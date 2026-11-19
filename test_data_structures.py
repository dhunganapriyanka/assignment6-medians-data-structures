
from elementary_data_structures import (
    MyArray, Matrix, Stack, Queue, LinkedList
)

from selection_algorithms import (
    median_of_medians,
    randomized_quickselect
)


def test_selection():
    numbers = [7, 2, 5, 2, 9, 1]

    for k in range(1, len(numbers) + 1):
        expected = sorted(numbers)[k - 1]

        assert median_of_medians(numbers, k) == expected
        assert randomized_quickselect(numbers, k) == expected

    print("Selection Algorithms: PASSED")


def test_array():
    arr = MyArray()
    arr.insert(10)
    arr.insert(20)
    assert arr.access(0) == 10

    arr.delete(10)
    assert arr.display() == [20]

    print("Array: PASSED")


def test_matrix():
    matrix = Matrix(2, 2)
    matrix.insert(0, 1, 15)

    assert matrix.access(0, 1) == 15

    matrix.delete(0, 1)
    assert matrix.access(0, 1) == 0

    print("Matrix: PASSED")


def test_stack():
    stack = Stack()

    assert stack.pop() is None

    stack.push(10)
    stack.push(20)

    assert stack.peek() == 20
    assert stack.pop() == 20
    assert stack.pop() == 10

    print("Stack: PASSED")


def test_queue():
    queue = Queue()

    assert queue.dequeue() is None

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20

    print("Queue: PASSED")


def test_linked_list():
    linked = LinkedList()

    linked.insert(10)
    linked.insert(20)
    linked.insert(30)

    assert linked.display() == [10, 20, 30]

    linked.delete(20)

    assert linked.display() == [10, 30]

    print("Linked List: PASSED")


if __name__ == "__main__":
    test_selection()
    test_array()
    test_matrix()
    test_stack()
    test_queue()
    test_linked_list()

    print("\nAll tests passed successfully!")
