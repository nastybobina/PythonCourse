class EmptyQueueException(Exception):
    pass

class Queue:
    """
    Основной класс
    """
    class Node:
        """
        Вспомогательный класс для узлов списка
        """
        def __init__(self, data=None, next_node=None, previous_node=None):
            self.data = data  # храним информацию
            self.next = next_node  # ссылка на следующий узел
            self.prev = previous_node  # Ссылка на предыдущий узел

    def __init__(self):
        self.start = Queue.Node() # ссылка на начало очереди
        self.end = Queue.Node()  # ссылка на конец очереди
        self.start.next = self.end
        self.end.prev = self.start
        self.queue_length = 0

    def enqueue(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Queue.Node(val, self.start.next, self.start)
        self.start.next.prev = new_node
        self.start.next = new_node
        self.queue_length += 1

    def dequeue(self):
        """
        возвращаем элемент return_val из начала списка с удалением из списка
        """
        remove_node = self.end.prev
        self.end.prev = remove_node.prev
        remove_node.prev.next = remove_node.next
        return_val = remove_node.data
        remove_node.next = None
        remove_node.prev = None
        self.queue_length -= 1
        return return_val

    def isEmpty(self):
        if self.queue_length == 0:
            raise EmptyQueueException
