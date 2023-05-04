import copy
import math
import random
import numpy
import heapq
import time
import itertools
import collections
file_path = "D:\\Users\\ADMIN\\Documents\\Tin hoc Dai Cuong's Files\\Buoi 3\\GA_Resupply\\TSPrd(time)\\Solomon\\10\\C101_0.5.dat"
def read_data(path):
    global data
    global number_of_cities
    global euclid_distance_matrix
    global manhattan_distance_matrix
    global city
    global release_date
    f = open(path)
    data = f.readlines()
    number_of_cities = int(data[0].split()[1])
    manhattan_distance_matrix = [0] * number_of_cities
    for i in range(number_of_cities):
        manhattan_distance_matrix[i] = [0] * number_of_cities
    euclid_distance_matrix = [0] * number_of_cities
    for i in range(number_of_cities):
        euclid_distance_matrix[i] = [0] * number_of_cities
    city = []
    for i in range(5, 5 + number_of_cities):
        city.append([])
        line = data[i].split()
        for j in range(0, 2):
            city[i - 5].append(float(line[j]))
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            euclid_distance_matrix[i][j] = euclid_distance(city[i], city[j])
    euclid_distance_matrix = numpy.array(euclid_distance_matrix)
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            manhattan_distance_matrix[i][j] = manhattan_distance(city[i], city[j])
    manhattan_distance_matrix = numpy.array(manhattan_distance_matrix)
    release_date = []
    for i in range(5, 5 + number_of_cities):
        release_date.append([])
        line = data[i].split()
        release_date[i - 5] = float(line[-1])
    return data
number_of_trucks = 3
number_of_drones = 3
truck_speed = 30
drone_speed = 60
drone_capacity = 4
drone_runtime = 3
def euclid_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
def manhattan_distance(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])
"""def convert(chromosome):
    array = []
    for i in range(number_of_trucks):
        array.append([])
    index = 0
    for i in range(len(chromosome)):
        if chromosome[i][0] != 0: array[index].append(chromosome[i])
        else: index = index + 1
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j][1] != 0: array[i][j][1] = array[i][array[i][j][1] - 1][0]
    for i in range(len(array)):
        array[i].insert(0, [0, -1])
    solution = copy.deepcopy(array)
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            solution[i][j][1] = []
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            for k in range(j, len(solution[i])):
                if array[i][k][1] == solution[i][j][0]: solution[i][j][1].append(array[i][k][0])
    return solution


def fitness_function(chromosome):
    solution = convert(chromosome)
    truck_time = []
    for i in range(number_of_trucks):
        truck_time.append([i, 0])
    drone_time = []
    for i in range(number_of_drones):
        drone_time.append([i, 0])
    return 0"""
# Ưu tiên Truck hơn.
def convert(chromosome):
    for i in range(len(chromosome[1])):
        chromosome[1][i] = [chromosome[0][element] for element in sorted([chromosome[0].index(item) for item in chromosome[1][i]])]
    result = []
    for i in range(len(chromosome[1])):
        result.append([])
        for j in range(0, len(chromosome[1][i]), drone_capacity):
            result[i].append(chromosome[1][i][j:j + drone_capacity])
    chromosome[1] = result
    chromosome_fake = copy.deepcopy(chromosome)

    return chromosome
read_data(file_path)
truck_route = [5,2,0,1,3,4,7,9,0,10,6,8]
drone_route = [[5,10],[2,9,3,8,6],[4]]
first = [truck_route, drone_route]
feed = convert(first)
"""xxx = convert(first)"""