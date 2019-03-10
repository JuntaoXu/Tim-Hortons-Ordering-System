# drive Module Juntao Xu Student: 20132432

'''
This is the module that drive the program
the program should have open connection to any website
read and process the commands one by one
'''

# the driver program should be a bunch of if statements
# if functionality belonging tob each if statement exceed split it into more modules
# all printing(output) should happen in this module

import urllib.request
import command


def organize_data(data):
    '''
    organize the data form the website
    input: information from the website
    output: organized queue which is format as a list of lists
    '''
    adjusted_content = ''
    adjusted_list = []

    # when me need to adjust the data commands
    if len(data) < 3:
        for element in data:
            adjusted_content = adjusted_content + element + ' '

        # change the flag to enter the second circumstance
        return adjusted_content[:-1]

    # when me need to adjust the data for order contents
    else:
        for element in data:
            # for the situation where we have %abc
            if element[0] == '%':
                # append the content stored and start a new content
                adjusted_list.append(adjusted_content[:-1])
                adjusted_content = ' '
                element = element[1:]
                adjusted_content = adjusted_content + element + ' '

            # for this situation we have abc%
            elif element[-1] == '%':
                element = element[:-1]
                adjusted_content = adjusted_content + element
                # append the content stored and start a new content
                adjusted_list.append(adjusted_content[1:])
                adjusted_content = ' '

            # for the situation where there isn't a % symbol in the element
            else:
                adjusted_content = adjusted_content + element + ' '

        # to append the price of the order to the list, otherwise it will fail to append
        adjusted_list.append(adjusted_content[1:-1])

        # change the flag to enter the first circumstance
        return adjusted_list


def readHtml():
    print('I\'ve added command name before each operation runs to make it easier to check')
    print('for performing linear search, list.index() is also a sort of linear search')
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/timOrders.txt")
    html = response.readline()  # reads one line
    # add a loop here to check to see if the content length of html is 0.  If not, continue
    all_orders = []
    while len(html) > 0:
        # splits this line into a list of "tokens"  (print it to see what you get)
        data = html.decode('utf-8').split()
        # at this point you have a list representing this command
        adjusted_data = organize_data(data)

        if data[0] == 'submit':
            print('command submit')
            raw_order = organize_data(data)
            all_orders, raw_queue, start = command.submit(raw_order, all_orders)
            print('Adding order', raw_queue[0][-1], 'to the queue with timestamp', start)

        else:
            if data[0] == 'complete':
                print('command complete')
                all_orders, element, time_spend = command.complete(all_orders)
                print('completed order', element[0][-1], 'in', time_spend)

            elif data[0] == 'queue':
                print('command queue')
                number_of_orders, total_value = command.queue_contents(all_orders)
                print('There are currently', number_of_orders, 'orders')
                print('The total value of orders are', total_value)

            elif data[0] == 'cancel':
                print('command cancel')
                # to process the necessary variables for the function
                for order in all_orders:
                    if order[0][-1] == data[1]:
                        target_order = order
                        command.cancel(all_orders, target_order)

                    # store the return of the function temporarily
                    memory = command.cancel(all_orders, target_order)

                    # to differentiate the return value
                    if len(memory) < 2:
                        print(print('unable to cancel job', memory, 'it has already been processed'))
                    else:
                        all_orders = memory

            elif data[0] == 'modify':
                print('command modify')
                for order in all_orders:
                    # to process the necessary variables for the function
                    if order[0][-1] == data[1]:
                        target_order = order
                        modified_order = organize_data(data)
                        command.modify(all_orders, target_order, modified_order[-2:])
                    memory1, memory2 = command.modify(all_orders, target_order, modified_order[-2:])
                    if memory1 == 1:
                        print('cannot modify order')
                    else:
                        all_orders = memory1
                        print('modified order', memory2)

            elif data[0] == 'next':
                print('command next')
                memory = command.next_order(all_orders)
                if memory == 1:
                    print('there isn\'t a next order')
                else:
                    print('the next order is', memory)

            elif data[0] == 'sleep':
                print('command sleep')
                command.sleep(data[1])

        # note that the food order isn't quite what you want, write a function that will fix it.
        # now take action depending on what the command is, for example removeFromQueue(101)
        # read another line
        html = response.readline()

readHtml()


# the flowing test code is for the organize data function, get rid of the quotations to activate it
'''
if __name__ == '__main__':
    # to check the organize_data function
    # while the function is reading the order instructions
    queue = ['queue', 'contents']
    a = organize_data(queue)
    print(a)
    print('should return queue contents')

    # while the function is reading the order detail
    queue = ['submit', '1', '%turkey', 'wrap', 'large', 'coffee%', '8.25']
    a = organize_data(queue)
    print(a)
    print('should print [\'submit 1\', \'turkey wrap large coffee\', \'8.25\']')
'''

