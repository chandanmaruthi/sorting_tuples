#
# Problem: Implement a function that takes a number of intervals,
#          finds all overlapping intervals, merges the overlapping
#          interval into a single interval and returns the merged
#          intervals in ascending order.
#
# Output: Print the input array with all intervals and the output
#         array of merged intervals
#
# Example:
# input = [(1, 3), (12, 14), (2, 4), (11, 15),
#          (8, 10), (9, 11), (10, 13), (5, 7), (16, 20)]
# expected = [(1,4), (5, 7), (8, 15), (16, 20)]
#
# Explanation:
# (1, 4)  -> (1, 3), (2, 4)
# (5, 7)  -> (5, 7)
# (8, 15) -> (12, 14), (11, 15), (8, 10), (9, 11), (10, 13)
# (16, 20) -> (16, 20)
#


import time
import timeit
import random
random.seed()


def gen_input(input_size:int):
    return [(random.randint(0, input_size), random.randint(0, input_size)) for k in range(input_size)]

def sort_tuples(input):
    for pointer in range(0, len(input)-1):
        if input[pointer][0]>input[pointer][1]:
            input[pointer] = (input[pointer][1], input[pointer][0])
    return input

def method_1():
    input.sort()
    pointer =0
    max_len=len(input)
    end_of_list= False
    did_something= False
    iteration = 0
    while True:
        iteration +=1
        if len(input)==1:
            return input
        cur_input = input[pointer]
        next_input = input[pointer+1]

        if cur_input[1]>= next_input[0]:
            did_something = True
            input[pointer]= (cur_input[0],next_input[1])
            input.pop(pointer+1)
            max_len = len(input)
        if pointer >= max_len - 2 :
            pointer = 0
            did_something = False

        else:
            pointer +=1



        if (pointer >= max_len - 2) and did_something==False:
            break
    return input

def method_2():
    input_orig = input

    pointer =0
    max_len=len(input)
    end_of_list= False
    did_something= False
    iteration = 0

    while True:
        iteration +=1
        cur_input = input[pointer]
        next_input = input[pointer+1]

        # if adjacent element is not overlapping and greater than current interval swap
        if cur_input[0]>= next_input[0] and cur_input[1] >=next_input[1]:
            did_something = True
            # Swap elements
            input.insert(pointer, next_input)
            input.pop(pointer+2)

        if cur_input[0] < next_input[0] and cur_input[1] > next_input[0]:
            did_something = True
            input[pointer] = (cur_input[0], next_input[1])
            input.pop(pointer+1)
            max_len = len(input)

        if pointer == max_len - 2:
            pointer = 0
            did_something = False
        else:
            pointer +=1
        if (pointer >= max_len - 2) and did_something==False:
            break
        if len(input)==1:
            return input
    return input



#input = [(1, 3), (12, 14), (2, 4), (11, 15), (8, 10), (9, 11), (10, 13), (5, 7), (16, 20)]
#expected = [(1, 4), (5, 7), (8, 15), (16, 20)]

divider = "---------------------------------------------------------------------------------"
print("Starting experiments")
input = sort_tuples(gen_input(10))
print(" Time taken to execute method_1  for list size {} time taken {}".format(10, timeit.timeit(stmt=method_1,number= 5)))
print(" Time taken to execute method_2  for list size {} times taken {}".format(10, timeit.timeit(stmt=method_2,number= 5)))
print(divider)
input_10 = sort_tuples(gen_input(100))
print(" Time taken to execute method_1  for list size {} times taken {}".format(100, timeit.timeit(stmt=method_1,number= 5)))
print(" Time taken to execute method_2  for list size {} times taken {}".format(100, timeit.timeit(stmt=method_2,number= 5)))
print(divider)
input_10 = sort_tuples(gen_input(1000))
print(" Time taken to execute method_1  for list size {} times taken {}".format(1000, timeit.timeit(stmt=method_1,number= 5)))
print(" Time taken to execute method_2  for list size {} times taken {}".format(1000, timeit.timeit(stmt=method_2,number= 5)))
print(divider)
input_10 = sort_tuples(gen_input(10000))
print(" Time taken to execute method_1  for list size {} times taken {}".format(10000, timeit.timeit(stmt=method_1,number= 5)))
print(" Time taken to execute method_2  for list size {} times taken {}".format(10000, timeit.timeit(stmt=method_2,number= 5)))
print(divider)
input_10 = sort_tuples(gen_input(100000))
print(" Time taken to execute method_1  for list size {} times taken {}".format(100000, timeit.timeit(stmt=method_1,number= 5)))
print(" Time taken to execute method_2  for list size {} times taken {}".format(100000, timeit.timeit(stmt=method_2,number= 5)))
print(divider)
input_10 = sort_tuples(gen_input(1000000))
print(" Time taken to execute method_1  for list size {} times taken {}".format(1000000, timeit.timeit(stmt=method_1,number= 5)))
print(" Time taken to execute method_2  for list size {} times taken {}".format(1000000, timeit.timeit(stmt=method_2,number= 5)))
print(divider)
