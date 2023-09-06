# Связный список - структура данных, представляющая собой набор узлов. Узел содержит значение и
# указатель на следующий узел. Первый узел в связном списке называется головным. Данные хранятся в
# непоследовательных ячейках памяти.

# Односвязный - указатель только на следующий элемент.
# Двусвязный - указатель на следующий и предыдущий.
# Круговой - последний указатель на первый элемент, а если двусвязный, то первый на последний.
class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    # конструктор, создающий головной элемент
    def __init__(self, is_double=False, is_circular=False):
        self.head = Node()
        self.size = 0
        self.is_double = is_double
        self.is_circular = is_circular

    # добавляет новый элемент в конец списка
    def append(self, value):
        self.size += 1

        current = self.head
        first = None
        previous = None
        c = 0

        while current.next is not None:
            if c == 1:
                first = current
            current = current.next
            c += 1

        if self.is_circular:
            current.next = Node(value=value, next=first)

        current.next = Node(value=value, next=None)

    # вставляет новый элемент на указанную позицию
    def insert(self, value, position):
        if position < 0 or position > self.size:
            raise ValueError("Invalid position")

        current = self.head
        c = 0
        first = None
        while current.next is not None or (current.next is not first and c != 1):
            if c == 1:
                first = current

            if c == position:
                new_node = Node(value=value, next=current.next)
                current.next = new_node
                self.size += 1
                return
            c += 1
            current = current.next

        if c == position:
            new_node = None
            # если односвязный
            if not self.is_double:
                new_node = Node(value=value, next=None)
            # если двусвязный
            if self.is_double:
                new_node = Node(value=value, next=first)
            current.next = new_node
            self.size += 1

    # удаляет первое вхождение элемента с указанным значением
    def remove(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is not None:
                    previous.next = current.next
                else:
                    # Если удаляем головной элемент, то обновляем голову списка
                    self.head = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

    # ищет элемент с указанным значением и возвращает его позицию
    def search(self, value):
        current = self.head
        c = 0
        pos = None
        while current is not None:
            if value == current.value:
                pos = c
            c += 1
            current = current.next

        return pos

    # возвращает значение элемента на указанной позиции
    def get(self, position):
        if position < 0 or position > self.size:
            raise IndexError("Invalid position")

        current = self.head
        c = 0
        val = None
        while current is not None:
            if c == position:
                val = current.value
            c += 1
            current = current.next

        return val

    # реверсия списка
    def reverse_list(self):
        current = self.head.next
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head.next = previous

    # создание цикла в односвязном списке
    def create_cycle(self):
        current = self.head
        first = None
        c = 0
        while current.next is not None:
            if c == 1:
                first = current
            current = current.next
            c += 1

        current = first
        self.is_circular = True

    # обнаружение цикла
    def detect_cycle(self):
        return self.is_circular

    # Метод для преобразования списка в двусвязный
    def create_double(self):
        if not self.is_double:  # Проверяем, не является ли уже двусвязным
            current = self.head
            previous = self.head
            next_node = self.head.next

            while current is not None:
                current.prev = previous
                previous = current
                current = next_node

                if next_node is not None:
                    next_node = next_node.next

            self.is_double = True

    def detect_double(self):
        return self.is_double

    # возвращает кол-во элементов в списке, не считая головной элемент
    def get_size(self):
        return self.size

    # проверяет, пуст ли список
    def is_empty(self):
        return self.size == 0

    # удаляет все элементы из списка, делая его пустым
    def clear(self):
        self.head = Node()
        self.size = 0

    # делает вывод красивым
    def __str__(self):
        values = []
        current = self.head.next
        out = ""
        first = None
        c = 0
        while current is not None or (current is not first and c != 1):
            if c == 1:
                first = current
            values.append(str(current.value))
            current = current.next

        bows = ""
        if self.is_double:
            bows = " <-> "
        else:
            bows = " -> "

        if self.is_circular:
            out = bows + bows.join(values) + bows
        else:
            out = bows.join(values)

        return out

# односвязный некольцованный
# list1 = LinkedList(is_circular=False, is_double=False)
# односвязный кольцованный
# list2 = LinkedList(is_circular=True, is_double=False)
# двусвязный некольцованный
# list3 = LinkedList(is_circular=False, is_double=True)
# двусвязный кольцованный
# list4 = LinkedList(is_circular=True, is_double=True)

