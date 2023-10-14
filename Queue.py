# Очередь - это структура данных, которая работает по принципу
# "первым вошел, первым вышел" (First-In-First-Out, FIFO).
# Элементы добавляются в конец очереди, а извлекаются из начала.
# Это означает, что элементы обрабатываются в порядке их добавления.

# Просто - элементы добавляются в конец, извлекаются из начала.

# Класс Нода - узла
class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Добавляет элемент в конец очереди (хвост).
    def enqueue(self, value):
        new_node = Node(value=value, next=None)

        if self.tail is None:
            # Если очередь пуста, устанавливаем и голову, и хвост на новый узел.
            self.head = new_node
            self.tail = new_node
        else:
            # Иначе добавляем новый узел в конец очереди и обновляем указатель на хвост.
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    # Удаляет и возвращает элемент из начала очереди (головы).
    def dequeue(self):
        if self.size == 0:
            return None
        
        removed_node = self.head
        self.head = self.head.next
        self.size -= 1

        return removed_node.value
    
    # Просмотр элемента из начала (головы) без удаления.
    def peek(self):
        if self.size == 0:
            return None
        
        return self.head.value
    
    # Проверяет, пуста ли очередь.
    def is_empty(self):
        return self.size == 0
    
    # Возвращается размер очереди.
    def get_size(self):
        return self.size
    
    # Красивый вывод очереди.
    def __str__(self):
        if self.size == 0:
            return "Queue is empty"

        current = self.head
        result = ""

        while current is not None:
            result += " " + str(current.value) + " "
            current = current.next

        return "Head ->" + result
        
# проверка методов
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(" ")

r = q.dequeue()
print(r)
print(q)
print(" ")

p = q.peek()
print(p)
print(q)
print(" ")

q1 = Queue()
print(q1.is_empty())
print(q1.get_size())
print(" ")

q2 = Queue()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
print(q2.is_empty())
print(q2.get_size())
