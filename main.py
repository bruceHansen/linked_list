import csv
import inspect
from linked_list import LinkedList

datacsv = open('data_example.csv')
datareader = csv.reader(datacsv, delimiter=' ')

line_number = 0
my_commands = []

csvfile = open('output.txt', 'w', newline='')

datawriter = csv.writer(csvfile, delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE)

for line in datareader:

    datawriter.writerow(['{}:{}'.format(line_number, line[0])])
    line_number += 1
    my_commands.append(line[0])

    #check which command is called

    if line[0].strip().split(',')[0] == 'CREATE':
        ll = LinkedList()

    elif line[0].strip().split(',')[0] == 'ADD':
        ll.add(line[0].strip().split(',')[1])

    elif line[0].strip().split(',')[0] == 'GET':
        datawriter.writerow([ll.get(line[0].strip().split(',')[1])])

    elif line[0].strip().split(',')[0] == 'DELETE':
        if ll.delete(line[0].strip().split(',')[1]):
            datawriter.writerow([ll.delete(line[0].strip().split(',')[1])])

    elif line[0].strip().split(',')[0] == 'SWAP':
        if ll.swap(line[0].strip().split(',')[1], line[0].strip().split(',')[2]):
            datawriter.writerow([ll.swap(line[0].strip().split(',')[1], line[0].strip().split(',')[2])])

    elif line[0].strip().split(',')[0] == 'SET':
        if ll.set(line[0].strip().split(',')[1], line[0].strip().split(',')[2]):
            datawriter.writerow([ll.set(line[0].strip().split(',')[1], line[0].strip().split(',')[2])])

    elif line[0].strip().split(',')[0] == 'INSERT':
        if ll.insert(line[0].strip().split(',')[1], line[0].strip().split(',')[2]):
            datawriter.writerow([ll.insert(line[0].strip().split(',')[1], line[0].strip().split(',')[2])])

    elif line[0].strip().split(',')[0] == 'DEBUG':
        datawriter.writerow([ll.debug_print()])

    else:
        datawriter.writerow(['no command found'])

