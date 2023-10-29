class EmptyStackException(Exception):
    pass

class Stack:
    """
    Основной класс для стека
    """
    class Node:
        """
        Вспомогательный класс для узлов списка
        """
        def __init__(self, data, next_elem):
            self.top_elem_data = data
            self.next_elem = next_elem

    def __init__(self):
        self.top_elem = None  # ссылка на конец стека

    def elemtIsEmpty(self):
        """
        проверка стека на пустоту
        """
        return self.top_elem is None

    def push(self, data):
        """
        добавление элемента val в конец списка
        """
        self.top_elem = Stack.Node(data, self.top_elem)

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.elemtIsEmpty():
            current_elem = self.top_elem.top_elem_data
            self.top_elem = self.top_elem.next_elem
            return current_elem
        else:
            raise EmptyStackException

    def peek(self):
        """
        вывод на печать содержимого стека
        """
        if not self.elemtIsEmpty():
            return self.top_elem.top_elem_data
        else:
            raise EmptyStackException
