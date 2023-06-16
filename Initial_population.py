import copy
import math
import random
import numpy
import heapq
import time
import itertools
import collections

import Data
import Fitness_function

def count_truck_path(route):
    sum = Fitness_function.max_release_date(route)
    route.append(0)
    route.insert(0, 0)
    for i in range(len(route) - 1):
        sum = sum + Data.manhattan_move_matrix[route[i]][route[i+1]]
    return sum

def initial_solution():
    truck_route = []
    for i in range(Data.number_of_trucks):
        truck_route.append([])
    compare = [0]*Data.number_of_trucks
    city = []
    for i in range(Data.number_of_cities - 1):
        city.append(i + 1)
    city = Fitness_function.sorted_by_release_date(city)
    for i in range(Data.number_of_cities - 1):
        for j in range(Data.number_of_trucks):
            temp = copy.deepcopy(truck_route[j])
            temp.append(city[i])
            compare[j] = count_truck_path(temp)
        value = min(compare)
        index = 0
        for j in range(Data.number_of_trucks):
            if compare[j] == value:
                index = j
                break
        truck_route[index].append(city[i])
    return truck_route

print("1 :",initial_solution())
'''x = initial_solution()'''
x = [[1, 2, 5, 3, 10], [4, 6, 7, 8], [9]]
def sort_truck_route(route):
    distance = []
    for i in range(len(route)):
        distance.append(Data.manhattan_move_matrix[0][Data.city[route[i]]])
    value = max(distance)
    index = 0
    for i in range(len(distance)):
        if distance[i] == value:
            index = i
            break
    return 0