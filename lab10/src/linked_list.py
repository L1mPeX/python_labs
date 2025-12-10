# src/lab10/linked_list.py
from typing import Any, Iterator, Optional


class Node:
    """
    Узел односвязного списка.

    Атрибуты:
        value: значение элемента
        next: ссылка на следующий узел или None
    """

    def __init__(self, value: Any):
        """
        Инициализация узла.

        :param value: значение элемента
        """
        self.value = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    Односвязный список, состоящий из узлов Node.

    Поддерживает операции добавления, вставки, удаления и итерирования.

    Атрибуты:
        head: указатель на первый узел списка или None
        tail: указатель на последний узел для ускорения append или None
        _size: количество элементов в списке
    """

    def __init__(self):
        """Создает пустой список."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0

    def append(self, value: Any) -> None:
        """
        Добавить элемент в конец списка за O(1).

        :param value: значение для добавления
        """
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None  # для проверки типа
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """
        Добавить элемент в начало списка за O(1).

        :param value: значение для добавления
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """
        Вставить элемент по индексу idx.

        :param idx: индекс вставки от 0 до len(list)
        :param value: значение для вставки
        :raises IndexError: если индекс вне диапазона [0, size]
        """
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of range")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        """
        Удалить элемент по индексу idx.

        :param idx: индекс удаляемого элемента
        :raises IndexError: если индекс вне диапазона [0, size-1]
        """
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")
        if idx == 0:
            assert self.head is not None
            self.head = self.head.next
            if self._size == 1:
                self.tail = None
        else:
            prev = self.head
            for _ in range(idx - 1):
                assert prev is not None
                prev = prev.next
            assert prev is not None and prev.next is not None
            prev.next = prev.next.next
            if idx == self._size - 1:
                self.tail = prev
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        """Итератор по значениям в списке от головы к хвосту."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        """Количество элементов в списке."""
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)})"

    def __str__(self) -> str:
        """Красивый текстовый вывод в формате: [A] -> [B] -> None"""
        parts = []
        current = self.head
        while current:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)
