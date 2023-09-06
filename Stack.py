# Стек - это абстрактная структура данных, которая следует принципу
# "последним вошел, первым вышел" (Last-In-First-Out, LIFO). Это означает,
# что элементы добавляются и удаляются только с одного конца стека,
# который называется вершиной стека.

# Просто - элементы добавляются и удаляются только сверху.
class Stack:
    # инициализация стека
    def __init__(self):
        self.items = []

    # добавляет новый элемент на вершину стека
    def push(self, value):
        self.items.append(value)

    # удаляет и возвращает элемент с вершины стека
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # возвращает элемент с вершины стека без удаления
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # проверяет, пуст ли стек
    def is_empty(self):
        return len(self.items) == 0

    # поиск элемента в стеке
    def search(self, value, default=None):
        try:
            return self.items.index(value)
        except ValueError:
            return default

    # создание стека из массива
    def init_from_array(self, array):
        self.items.extend(array)

    # создание стека из связного списка
    def init_from_linked_list(self, linked_list):
        current = linked_list.head.next
        while current:
            self.items.append(current.value)
            current = current.next

    # для красивого вывода
    def __str__(self):
        return ", ".join(map(str, self.items))

    # возвращает размер стека
    def __len__(self):
        return len(self.items)

    # метод преобразования из Стека в список
    def __iter__(self):
        return iter(self.items)
