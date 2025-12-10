#!/bin/bash

echo "Testing Queue..."

python3 - << EOF
from structures import Queue

q = Queue()
assert q.is_empty()
q.enqueue('a')
q.enqueue('b')
assert q.peek() == 'a'
assert len(q) == 2
assert q.dequeue() == 'a'
assert q.dequeue() == 'b'
assert q.is_empty()

try:
    q.dequeue()
    print("Failed: no exception on dequeuing empty queue")
    exit(1)
except IndexError:
    pass

print("Queue tests passed.")
EOF
