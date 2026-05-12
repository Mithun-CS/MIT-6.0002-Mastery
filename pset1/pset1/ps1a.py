###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:Mithun
# Collaborators:None
# Time:

from audioop import reverse
#from sys import last_type
from typing import ByteString
from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    dict_map = {}
    with open(filename,"r") as given_file:
        for i in given_file:
            x,y = i.strip().split(",")
            dict_map[x] = int(y)
    return dict_map

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    rst = []
    lst = [i for i in cows.items()]
    sort_lst = sorted(lst, key = lambda x : x[1], reverse=True)
    while len(sort_lst) > 0:
        count = 0
        temp_lst =[]
        for i in sort_lst:
            if (count+ i[1]) <= limit:
                temp_lst.append(i[0])
                count += i[1]
        sort_lst = [i for i in sort_lst if i[0] not in temp_lst]        
        rst.append(temp_lst)
    return rst
    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best_plan = None
    lst = get_partitions(cows.keys())
    for i in lst:
        valid_partition = True
        for j in i:
            total_wg = 0
            for cow in j:
                total_wg += cows[cow]
                if total_wg > limit:
                    valid_partition = False
                    break
        if valid_partition:
            if best_plan is None or len(i) < len(best_plan):
                best_plan = i
    return best_plan

    
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    limit = 10

    start = time.time()
    greedy_results = greedy_cow_transport(cows,limit)
    end = time.time()
    print("Greedy Trips :",len(greedy_results))
    print("Greedy Time:", end - start)

    start = time.time()
    brute_results = brute_force_cow_transport(cows,limit)
    end = time.time()
    print("Brute Force Trips:", len(brute_results))
    print("Brute Force Time:", end - start)

compare_cow_transport_algorithms()


