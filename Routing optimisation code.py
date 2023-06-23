import math
import itertools

places = {
    'S1': (10, 20),
    'H1': (5, 11),
    'H2': (15, 30),
    'H3': (25, 15),
    'H4': (20, 5),
    'G1': (10, 5)
}

def Optimal(places):
    places_list = list(places.keys())
    places_list.remove('S1') 
    permutations1 = itertools.permutations(places_list)
    permutations2 = itertools.permutations(places_list+["G1"])
    permutations3 = itertools.permutations(places_list + ["G1","G1"])
    permutations4 = itertools.permutations(places_list + ["G1","G1","G1"])
    permutations = []
    
    for path in permutations1:
        if path[0] == "G1":
            continue
        if path[-1] == "G1":
            continue
        permutations.append(path)
    for path in permutations2:
        breach = 0
        if path[0] == "G1":
            continue
        for i in range(0,len(path)-1):
            if path[i] == path[i+1]:
                breach = 1
        if breach != 1:
            permutations.append(path)
    for path in permutations3:
        breach = 0
        if path[0] == "G1":
            continue
        for i in range(0,len(path)-1):
            if path[i] == path[i+1]:
                breach = 1
        if breach != 1:
            permutations.append(path)
    for path in permutations4:
        breach = 0
        if path[0] == "G1":
            continue
        for i in range(0,len(path)-1):
            if path[i] == path[i+1]:
                breach = 1
        if breach != 1:
            permutations.append(path)

    optimal_total_distance = math.inf
    optimal_path = None
    for path in permutations:
        total_distance = 0
        current_place = 'S1'
        picked = 0
        for next_place in path:
            if picked == 3: 
                total_distance += math.sqrt((places[current_place][0] - places['G1'][0]) ** 2 + (places[current_place][1] - places['G1'][1]) ** 2)
                picked = 0
                current_place = next_place
                continue
            if next_place == 'G1':  
                total_distance += math.sqrt((places[current_place][0] - places[next_place][0]) ** 2 + (places[current_place][1] - places[next_place][1]) ** 2)
                picked = 0
                current_place = next_place
                continue
            if picked < 3: 
                total_distance += math.sqrt((places[current_place][0] - places[next_place][0]) ** 2 + (places[current_place][1] - places[next_place][1]) ** 2)
                picked += 1
                current_place = next_place
                continue
        total_distance += math.sqrt((places[current_place][0] - places['G1'][0]) ** 2 + (places[current_place][1] - places['G1'][1]) ** 2)
        if total_distance <  optimal_total_distance:
            optimal_total_distance = total_distance
            optimal_path = path
    optimal_path = ["S1"] + list(optimal_path)
    if optimal_path[-1] != "G1":
        optimal_path = optimal_path + ["G1"]
    print("Optimal traversal path --->",optimal_path)
    print("Optimal distance --------->",optimal_total_distance)
    
Optimal(places)

