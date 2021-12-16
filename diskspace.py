from collections import deque
def segment(x, space):
    queue, response = deque(), -1
    for index, value in enumerate(space):
        if queue and queue[0] == index - x:
            queue.popleft()
        while queue and space[queue[-1]] > value:
            queue.pop()
        queue.append(index)
        if index >= x-1 and space[queue[0]] > response:
            response = space[queue[0]]
    return response
