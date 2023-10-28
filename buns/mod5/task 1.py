class EmptyStackException(Exception):
    pass

class Stack:

    class Node:
        def __init__(self, data, next_elem):
            self.top_elem_data = data
            self.next_elem = next_elem

    def __init__(self):
        self.top_elem = None

    def elemtIsEmpty(self):
        return self.top_elem is None

    def push(self, data):
        self.top_elem = Stack.Node(data, self.top_elem)

    def pop(self):
        if self.elemtIsEmpty():
            current_elem = self.top_elem.top_elem_data
            self.top_elem = self.top_elem.next_elem
            return current_elem
        else:
            raise EmptyStackException

    def peek(self):
        if not self.elemtIsEmpty():
            return self.top_elem.top_elem_data
        else:
            raise EmptyStackException
