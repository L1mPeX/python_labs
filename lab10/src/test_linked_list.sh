#!/bin/bash

echo "Testing SinglyLinkedList..."

python3 - << EOF
from linked_list import SinglyLinkedList

lst = SinglyLinkedList()
assert len(lst) == 0

lst.append(1)
lst.prepend(0)
lst.append(2)
assert list(lst) == [0, 1, 2]

lst.insert(1, 5)
assert list(lst) == [0, 5, 1, 2]

lst.remove_at(1)
assert list(lst) == [0, 1, 2]

try:
    lst.insert(10, 100)
    print("Failed: no exception on insert out of range")
    exit(1)
except IndexError:
    pass

try:
    lst.remove_at(10)
    print("Failed: no exception on remove_at out of range")
    exit(1)
except IndexError:
    pass

print("SinglyLinkedList tests passed.")
EOF
