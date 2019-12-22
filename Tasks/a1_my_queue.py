"""
My little Queue
"""
from typing import Any

_queue = []


def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	_queue.append(elem)
	print(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if no elements.

	:return: dequeued element
	"""
	if _queue:
		return _queue.pop()


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	print(ind)
	if _queue and ind in range(len(_queue)):
		return _queue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	return _queue.clear()
