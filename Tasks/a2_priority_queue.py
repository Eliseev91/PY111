"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any, List
import heapq

_priority_queue: List = []

def enqueue(elem: Any, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	heapq.heappush(_priority_queue, (priority, elem))
	return


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if not elements.

	:return: dequeued element
	"""
	if _priority_queue:
		return heapq.heappop(_priority_queue)


def peek(ind: int = 0, priority: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	if _priority_queue and ind in range(len(_priority_queue)):
		return _priority_queue[ind]

def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	return _priority_queue.clear()
