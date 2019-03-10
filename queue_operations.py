# queue Module Juntao Xu Student: 20132432

'''
This is the module that implements the functionality of a queue
- add to the queue
- delete from the queue
- provide the size of the queue
- indicate if the queue is empty
- what's the next item in the queue
'''

# NO PRINT STATEMENTS IN THIS MODULE


def enqueue(queue, queue_append):
    '''
    add to the queue
    input: queue
    output: a new queue with an additional element
    '''
    queue.append(queue_append)
    return queue


def dequeue(queue, target_queue):
    '''
    delete from the queue
    input: queue
    output: a new queue with one one less element
    '''
    queue.pop(queue.index(target_queue))
    return queue


def size(queue):
    '''
    check the size of the queue
    input: queue
    output: the size opf the queue
    '''
    queue_size = len(queue)
    return queue_size


def is_empty(queue_size):
    '''
    check if the queue is empty
    input: queue
    outputL: True or False (whether the queue is empty)
    '''
    if len(queue_size) == 0:
        return True
    return False


def look(queue):
    '''
    check the next element in the queue
    input: queue
    output: the second element in the queue
    '''
    return queue[1]


if __name__ == '__main__':
    print('The following are the testing materials')
    queue = [['a'],['b']]
    queue_append = ['c']
    target_queue = ['a']
    empty_list = []

    print()
    print('The following is the testing code part')

    # enqueue function
    print(enqueue(queue, queue_append))
    print('should return list containing abc')

    # dequeue function
    queue = [['a'], ['b']]   # define the variable again since it has been changed in the previous function
    print(dequeue(queue, target_queue))
    print('should return a list of list containing b')

    # size function
    queue = [['a'], ['b']]  # define the variable again since it has been changed in the previous function
    print(size(queue))
    print('should return 2')

    # is_empty function
    print(is_empty(queue))
    print('should return False')
    print(is_empty(empty_list))
    print('should return True')

    # look function
    print(look(queue, target_queue))
    print('should return a list containing b')
