# command Module Juntao Xu Student: 20132432

'''
this module calls the functions in the queue module
other functionality such as modifying orders and canceling orders will go into this function
each data in the queue should store the order ID, a timestamp, the contents of the order, price of the order
example of a queue = [id, timestamp, order contents, price]
'''

# need to perform linear search
# DO NOT duplicate the code in multiple functions
# THERE ARE NO USER INPUT IN THIS PROGRAM

'''
- SUBMIT indicates the cashier has received an order and is passing it to the chef
    ex: submit 101 %grilled cheese, broccoli soup, medium decaf% 12.95
    keyword, content, price
  Add a time stamp to the order
  the % should not be stored
  figure out what python module can be used to add timestamp
  program should print(Adding order XXX(id) to the queue with timestamp YYY(time order submitted)

- COMPLETE indicates that the next order has been completed
  should print(completed order XXX(id) in YYY(seconds))
  figure out the python module that finds out the current time

- Queue Contents
  print the number of orders currently in the queue and the total value of the orders
  should print(total number of orders: XX total value: YY)
  MUST NOT STORE RUNNING TOTAL IN THE PROGRAM

- Cancel
  remove an order from the program
  if job not on the queue, print(unable to cancel job XX, it has already been processed

- Modify
  find the order and replace the old content with new ones, change the price as well
  if not exist, print(cannot modify order)
  elif modified print(modified order XXX)
  timestamp remain unchanged

- Next Order
  print the next order
  should print(next order is XXX: YYY)
  if there are no orders in the queue print(no orders remaining)

- Sleep
  you should have your program rest for the time XX(seconds) specified
  find a python module that does this
  print nothing on the screen when the program is asleep
'''


import queue_operations
from datetime import datetime
import time


def submit(raw_queue, all_orders):
    # add the timestamp
    start = datetime.now()
    # submit the new
    modified_queue = queue_operations.enqueue(raw_queue, start)
    # append the order with timestamp to all orders
    all_orders.append(modified_queue)
    return all_orders, raw_queue, start


def complete(all_orders):
    # figure out the current time
    end = datetime.now()
    element = all_orders[0]
    # delete the order from al orders
    all_orders.pop(0)
    # to find the same order in all orders
    element.append(end)
    time_spend = element[-1] - element[-2]
    return all_orders, element, time_spend


def queue_contents(all_orders):
    number_of_orders = queue_operations.size(all_orders)
    total_value = 0
    # loop for calculating the sum
    for order in all_orders:
        total_value = total_value + float(order[-2])
    return number_of_orders, total_value


def cancel(all_orders, target_orders):
    # try if we can cancel the order
    try:
        all_orders = queue_operations.dequeue(all_orders, target_orders)
        return all_orders
    except:
        return target_orders[0][-1]


def modify(all_orders, target_order, modified_order):
    # try if we can find the order
    try:
        position = all_orders.index(target_order)
        # if found modify the
        all_orders[position][1] = modified_order[0]
        all_orders[position][2] = modified_order[1]
        return all_orders, target_order[0][-1]
    except:
        return 1, 2


def next_order(all_orders):
    try:
        next_order = queue_operations.look(all_orders)
        return next_order
    except:
        return 1


def sleep(sleep_time):
    time.sleep(int(sleep_time))


if __name__ == '__main__':
    # test for the sumbit function
    print()
    raw_queue = ['submit 1', 'turkey wrap large coffee', '8.25']
    all_orders = []
    print(submit(raw_queue, all_orders))
    print('should return submit 1 in a list of list, a raw queue with a timestamp and another timestamp')

    # test for the complete function
    print()
    all_orders = [['submit 1', 'turkey wrap large coffee', '8.25']]
    all_orders[0].append(datetime.now())
    print(complete(all_orders))
    print('should return the time spend for completing the order and return an empty list')

    # test for the queue_contents function
    print()
    all_orders = [['submit 1', 'turkey wrap large coffee', '8.25', 'timestamp'], ['submit 2', 'mushroom soup chocolate dip donut', '7.59', 'timestamp']]
    print(queue_contents(all_orders))
    print('should return 2 and the current order and the combined value of all orders')

    # test of the cancel function
    print()
    all_orders = [['submit 1', 'turkey wrap large coffee', '8.25', 'timestamp'], ['submit 2', 'mushroom soup chocolate dip donut', '7.59', 'timestamp']]
    target_order = ['submit 1', 'turkey wrap large coffee', '8.25', 'timestamp']
    print(cancel(all_orders, target_order))
    print('should return the orders left in all orders after deleting target order')

    all_orders = [['submit 1', 'turkey wrap large coffee', '8.25', 'timestamp'], ['submit 2', 'mushroom soup chocolate dip donut', '7.59', 'timestamp']]
    target_order = ['submit 3', 'ham and swiss chocolate milk', '8.29', 'timestamp']
    print(cancel(all_orders, target_order))
    print('should return None')

    # test for the modify order function
    print()
    all_orders = [['submit 1', 'turkey wrap large coffee', '8.25', 'timestamp 1'], ['submit 2', 'mushroom soup chocolate dip donut', '7.59', 'timestamp 1']]
    target_order = ['submit 1', 'turkey wrap large coffee', '8.25', 'timestamp 1']
    modified_order = ['ham and swiss chocolate milk', '8.29']
    print(modify(all_orders, target_order, modified_order))
    print('should return orders containing submit 1 and timestamp 1')

    all_orders = [['submit 1', 'turkey wrap large coffee', '8.25', 'timestamp 1'], ['submit 2', 'mushroom soup chocolate dip donut', '7.59', 'timestamp 1']]
    target_order = ['submit 3', 'ham and swiss chocolate milk', '8.29', 'timestamp 2']
    modified_order = ['turkey wrap large coffee', '8.25']
    modify(all_orders, target_order, modified_order)
    print('should print cannot modify order')

    # test for the next order function
    print()
    all_orders = [['submit 1', 'turkey wrap large coffee', '8.25', 'timestamp'], ['submit 2', 'mushroom soup chocolate dip donut', '7.59', 'timestamp']]
    next_order(all_orders)
    print('should return submit 2 order')

    all_orders = [['submit 3', 'ham and swiss chocolate milk', '8.29']]
    next_order(all_orders)
    print('should print no orders remaining')

    # test for the sleep function
    print()
    sleep_time = 5
    sleep(sleep_time)
    print('the function should print this after sleeping for 5 seconds')