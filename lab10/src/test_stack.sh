#!/bin/bash

echo "Testing Stack..."

python3 - << EOF
from structures import Stack

s = Stack()
assert s.is_empty()
s.push(1)
s.push(2)
assert s.peek() == 2
assert len(s) == 2
assert s.pop() == 2
assert s.pop() == 1
assert s.is_empty()

try:
    s.pop()
    print("Failed: no exception on popping empty stack")
    exit(1)
except IndexError:
    pass

print("Stack tests passed.")
EOF
