def dequeue(queue):
    length = len(queue)
    if length > 1:
        return queue[0], queue[1:]
    elif length == 1:
        return queue[0], []
    else:
        return None, None
        
def enqueue(queue, element):
    queue.append(element)
    return queue

def isEmpty(queue):
    if len(queue) > 0:
        return False
    return True

def look(queue):
    if len(queue) > 0:
        return queue[0]
    return None

def size(queue):
    return len(queue)

if __name__ == "__main__":
    q = [list(range(3)), list(range(3, 6)), list(range(6, 9))]
    print(f"queue q: {q}")
    element, newQ = dequeue(q)
    print(f"dequeue q: new queue: {newQ}, element: {element}")
    addElementQ = enqueue(newQ, element)
    print(f"enqueue q: addElementQ: {addElementQ}")
    print(f"check whether addElementQ is empty: {isEmpty(addElementQ)}")
    addElementQ = []
    print(f"addElementQ: {addElementQ}")
    print(f"check whether addElementQ is empty: {isEmpty(addElementQ)}")
    print(f"next element of q: {look(q)}")
    print(f"size of q: {size(q)}")
