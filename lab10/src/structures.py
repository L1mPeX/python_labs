from collections import deque
from typing import Any, Optional


class Stack:
    """
    Структура данных "Стек" (LIFO) на базе list.
    Вершина стека — последний элемент списка.
    """

    def __init__(self):
        """Создает пустой стек."""
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """
        Добавить элемент item на вершину стека.

        :param item: элемент для добавления
        """
        self._data.append(item)

    def pop(self) -> Any:
        """
        Удалить и вернуть верхний элемент стека.

        :raises IndexError: если стек пуст
        :return: верхний элемент
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        """
        Вернуть верхний элемент без удаления.

        :return: верхний элемент или None, если стек пуст
        """
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """
        Проверить, пуст ли стек.

        :return: True если пуст, иначе False
        """
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в стеке."""
        return len(self._data)


class Queue:
    """
    Структура данных "Очередь" (FIFO) на базе collections.deque.
    Голова очереди – левый край deque.
    """

    def __init__(self):
        """Создает пустую очередь."""
        self._data = deque()

    def enqueue(self, item: Any) -> None:
        """
        Добавить элемент в конец очереди.

        :param item: элемент для добавления
        """
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Удалить и вернуть элемент из начала очереди.

        :raises IndexError: если очередь пуста
        :return: первый элемент очереди
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
        """
        Вернуть первый элемент без удаления.

        :return: первый элемент или None, если очередь пуста
        """
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """
        Проверить, пуста ли очередь.

        :return: True если пуста, иначе False
        """
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в очереди."""
        return len(self._data)
