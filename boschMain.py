"""
Simple Program to help you get started with Google's APIs
"""
import urllib.request, json
import math
from random import randint
import  copy




data = {}
data['API_key'] = 'AoRQLJZ4fFULwmeEEPFHMFVwAV5EAoPJ_r4EmLrPm2tDnpUgPQtzbSh5pcOx1Rg9'
data['addresses'] = {
    'Bosch Bidadi': ['12.797118', '77.423885'],
    'RR nagar busStop': ['12.914682', '77.520583'],
    'KathriGuppe Circle': ['12.925495', '77.550119'],
    'JayaNagar': ['12.9279', '77.58355'],
    'Kadirenahalli': ['12.915613', '77.561685'],
    'Mantri Apartment': ['12.937671', '77.585208'],
    'Kodipalya': ['12.912695', '77.520808'],
    'Uttrahalli road': ['12.912444', '77.485435'],
    'Devegowda': ['12.921923', '77.56051'],
    'RNSIT': ['12.90322', '77.516645'],
    'Kamakya': ['12.923769', '77.554121'],
    'PESIT': ['12.934796', '77.5371'],
    'Ittamadu': ['12.923999', '77.543628'],
    'Hosakarehalli': ['12.930326', '77.539626'],
    'Kathreguppe ': ['12.924313', '77.55263'],
    #'Rajarajeshwari':['12.81136','77.57837'],
    'Rajarajeshwari': ['12.930221', '77.506024'],
    'Jantha': ['12.976791', '77.579634'],
    'Bata Show Room': ['12.923733', '77.569355'],
    'Kanthi Sweets': ['12.914666', '77.520593'],
    'Chowdeshwari talkies': ['12.915027', '77.551986']
}

numberPassenger=92
occupancy=32
minOccupancy=math.ceil(85/100*float(occupancy))
minBuses=math.ceil(numberPassenger/occupancy)



DistanceMatrix = []
places = []
coordinates = []
UTM = []


DistanceMatrix=[[0, 24.24, 31.3, 37.1, 34.06, 33.57, 24.47, 17.71, 32.97, 21.79, 32.97, 29.79, 31.37, 30.73, 31.84, 20.86, 32.4, 34.81, 24.24, 32.94],
[24.24, 0, 5.33, 11.13, 6.13, 12.43, 0.23, 5.61, 7.0, 1.83, 7.0, 5.15, 4.79, 3.46, 5.87, 4.29, 13.28, 8.84, 0.0, 5.34],
[31.3, 5.33, 0, 5.82, 2.78, 5.28, 5.55, 9.46, 1.69, 5.88, 1.69, 1.88, 1.32, 1.87, 0.56, 7.44, 11.96, 3.53, 5.33, 1.66],
[37.1, 11.13, 5.82, 0, 4.0, 1.72, 10.88, 15.26, 4.67, 9.89, 5.37, 7.69, 7.13, 7.67, 5.82, 13.25, 7.23, 2.89, 11.13, 5.67],
[34.06, 6.13, 2.78, 4.0, 0, 5.27, 6.49, 12.22, 1.36, 5.9, 2.33, 4.64, 4.08, 4.63, 2.78, 10.2, 11.81, 2.1, 6.13, 1.67],
[33.57, 12.43, 5.28, 1.72, 5.27, 0, 12.66, 15.88, 4.45, 10.86, 5.42, 7.0, 6.66, 6.98, 5.3, 13.86, 7.08, 3.81, 12.43, 6.14],
[24.47, 0.23, 5.55, 10.88, 6.49, 12.66, 0, 5.61, 7.23, 1.61, 7.23, 5.38, 5.15, 3.68, 6.1, 4.52, 13.51, 8.59, 0.23, 5.7],
[17.71, 5.61, 9.46, 15.26, 12.22, 15.88, 5.61, 0, 11.13, 4.08, 11.13, 7.95, 9.53, 8.22, 10.0, 3.16, 14.71, 12.97, 5.61, 11.1],
[32.97, 7.0, 1.69, 4.67, 1.36, 4.45, 7.23, 11.13, 0, 6.43, 1.24, 3.56, 3.0, 3.54, 1.69, 9.11, 10.61, 2.1, 7.0, 1.7],
[21.79, 1.83, 5.88, 9.89, 5.9, 10.86, 1.61, 4.08, 6.43, 0, 6.89, 6.86, 4.56, 5.29, 6.89, 5.32, 14.38, 7.94, 1.83, 5.11],
[32.97, 7.0, 1.69, 5.37, 2.33, 5.42, 7.23, 11.13, 1.24, 6.89, 0, 3.56, 3.0, 3.54, 1.69, 9.11, 10.35, 3.08, 7.0, 2.26],
[29.79, 5.15, 1.88, 7.69, 4.64, 7.0, 5.38, 7.95, 3.56, 6.86, 3.56, 0, 1.96, 1.31, 2.43, 5.93, 10.45, 5.4, 5.15, 3.52],
[31.37, 4.79, 1.32, 7.13, 4.08, 6.66, 5.15, 9.53, 3.0, 4.56, 3.0, 1.96, 0, 1.94, 1.87, 7.52, 12.04, 4.84, 4.79, 2.03],
[30.73, 3.46, 1.87, 7.67, 4.63, 6.98, 3.68, 8.22, 3.54, 5.29, 3.54, 1.31, 1.94, 0, 2.42, 6.2, 11.39, 5.38, 3.46, 3.51],
[31.84, 5.87, 0.56, 5.82, 2.78, 5.3, 6.1, 10.0, 1.69, 6.89, 1.69, 2.43, 1.87, 2.42, 0, 7.99, 10.35, 3.53, 5.87, 1.66],
[20.86, 4.29, 7.44, 13.25, 10.2, 13.86, 4.52, 3.16, 9.11, 5.32, 9.11, 5.93, 7.52, 6.2, 7.99, 0, 12.69, 10.96, 4.29, 9.08],
[32.4, 13.28, 11.96, 7.23, 11.81, 7.08, 13.51, 14.71, 10.61, 14.38, 10.35, 10.45, 12.04, 11.39, 10.35, 12.69, 0, 8.09, 13.28, 13.6],
[34.81, 8.84, 3.53, 2.89, 2.1, 3.81, 8.59, 12.97, 2.1, 7.94, 3.08, 5.4, 4.84, 5.38, 3.53, 10.96, 8.09, 0, 8.84, 3.6],
[24.24, 0.0, 5.33, 11.13, 6.13, 12.43, 0.23, 5.61, 7.0, 1.83, 7.0, 5.15, 4.79, 3.46, 5.87, 4.29, 13.28, 8.84, 0, 5.34],
[32.94, 5.34, 1.66, 5.67, 1.67, 6.14, 5.7, 11.1, 1.7, 5.11, 2.26, 3.52, 2.03, 3.51, 1.66, 9.08, 13.6, 3.6, 5.34, 0]]


TimeMatrix=[[0, 39.22, 40.58, 52.54, 44.06, 53.88, 39.57, 29.4, 41.45, 36.85, 41.45, 38.42, 40.91, 39.55, 40.82, 32.05, 49.03, 47.14, 39.22, 47.52],
[39.22, 0, 14.61, 26.57, 14.37, 27.44, 0.4, 10.35, 15.47, 4.08, 15.48, 12.5, 11.65, 9.32, 14.84, 8.25, 23.27, 21.17, 0.0, 14.38],
[40.58, 14.61, 0, 15.04, 6.56, 15.28, 15.02, 13.93, 3.95, 15.98, 3.68, 5.11, 5.37, 5.28, 3.03, 12.13, 20.26, 9.64, 14.61, 10.02],
[52.54, 26.57, 15.04, 0, 12.8, 5.96, 26.54, 25.89, 12.94, 26.13, 13.19, 17.07, 17.33, 17.24, 13.75, 24.1, 17.45, 9.71, 26.57, 19.07],
[44.06, 14.37, 6.56, 12.8, 0, 16.17, 14.38, 17.41, 4.63, 13.32, 4.71, 8.58, 8.85, 8.76, 5.27, 15.62, 24.04, 7.69, 14.37, 6.25],
[53.88, 27.44, 15.28, 5.96, 16.17, 0, 27.86, 25.76, 13.99, 28.66, 15.29, 18.61, 18.75, 18.78, 15.28, 23.96, 14.77, 12.18, 27.44, 21.26],
[39.57, 0.4, 15.02, 26.54, 14.38, 27.86, 0, 10.35, 15.89, 3.66, 15.9, 12.92, 11.67, 9.73, 15.26, 8.67, 23.68, 21.13, 0.4, 14.38],
[29.4, 10.35, 13.93, 25.89, 17.41, 25.76, 10.35, 0, 14.81, 7.43, 14.8, 11.77, 14.26, 12.59, 14.17, 3.93, 20.91, 20.49, 10.36, 20.11],
[41.45, 15.47, 3.95, 12.94, 4.63, 13.99, 15.89, 14.81, 0, 15.81, 2.1, 5.98, 6.23, 6.15, 2.66, 13.02, 21.01, 5.83, 15.48, 8.33],
[36.85, 4.08, 15.98, 26.13, 13.32, 28.66, 3.66, 7.43, 15.81, 0, 15.8, 15.06, 10.61, 13.39, 15.81, 10.18, 25.22, 20.86, 4.06, 13.32],
[41.45, 15.48, 3.68, 13.19, 4.71, 15.29, 15.9, 14.8, 2.1, 15.8, 0, 5.98, 6.24, 6.15, 2.66, 13.01, 20.23, 7.79, 15.48, 8.95],
[38.42, 12.5, 5.11, 17.07, 8.58, 18.61, 12.92, 11.77, 5.98, 15.06, 5.98, 0, 5.44, 4.08, 5.34, 9.97, 18.51, 11.68, 12.51, 12.05],
[40.91, 11.65, 5.37, 17.33, 8.85, 18.75, 11.67, 14.26, 6.23, 10.61, 6.24, 5.44, 0, 5.61, 5.6, 12.47, 21.0, 11.93, 11.66, 9.41],
[39.55, 9.32, 5.28, 17.24, 8.76, 18.78, 9.73, 12.59, 6.15, 13.39, 6.15, 4.08, 5.61, 0, 5.52, 10.8, 19.64, 11.84, 9.32, 12.22],
[40.82, 14.84, 3.03, 13.75, 5.27, 15.28, 15.26, 14.17, 2.66, 15.81, 2.66, 5.34, 5.6, 5.52, 0, 12.38, 20.22, 8.35, 14.84, 8.73],
[32.05, 8.25, 12.13, 24.1, 15.62, 23.96, 8.67, 3.93, 13.02, 10.18, 13.01, 9.97, 12.47, 10.8, 12.38, 0, 19.12, 18.69, 8.25, 19.08],
[49.03, 23.27, 20.26, 17.45, 24.04, 14.77, 23.68, 20.91, 21.01, 25.22, 20.23, 18.51, 21.0, 19.64, 20.22, 19.12, 0, 19.93, 23.27, 27.62],
[47.14, 21.17, 9.64, 9.71, 7.69, 12.18, 21.13, 20.49, 5.83, 20.86, 7.79, 11.68, 11.93, 11.84, 8.35, 18.69, 19.93, 0, 21.18, 13.7],
[39.22, 0.0, 14.61, 26.57, 14.37, 27.44, 0.4, 10.36, 15.48, 4.06, 15.48, 12.51, 11.66, 9.32, 14.84, 8.25, 23.27, 21.18, 0, 14.38],
[47.52, 14.38, 10.02, 19.07, 6.25, 21.26, 14.38, 20.11, 8.33, 13.32, 8.95, 12.05, 9.41, 12.22, 8.73, 19.08, 27.62, 13.7, 14.38, 0]]

for place, coordinate in data['addresses'].items():
    places.append(place)
    coordinates.append(coordinate)





#CODE FOR CREATING TIME AND DISTANCE MATRIX

# for places, coordinate in data['addresses'].items():
#     row = []
#     row2=[]
#     originStr = coordinate[0] + "," + coordinate[1]
#     destinationStr = ""
#
#     for i in range(20):
#         if i != 19:
#             destinationStr += coordinates[i][0] + "," + coordinates[i][1] + ";"
#         else:
#             destinationStr += coordinates[i][0] + "," + coordinates[i][1]
#     # print(destinationStr)
#     url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=" + originStr + "&destinations=" + destinationStr + "&travelMode=driving&key=" + \
#           data['API_key']
#     # print(url)
#     response = urllib.request.urlopen(url).read()
#     # sleep(randint(8,15))
#     directions = json.loads(response)
#     for x in directions['resourceSets'][0]['resources'][0]['results']:
#         row.append(x['travelDistance'])
#         row2.append(x['travelDuration'])
#
#     # print(row)
#     DistanceMatrix.append(row)
#     TimeMatrix.append(row2)
#
# for i in range(20):
#     for j in range(20):
#         if i > j:
#             x = (DistanceMatrix[i][j] + DistanceMatrix[j][i]) / 2
#             x = float("{0:.2f}".format(x))
#             DistanceMatrix[i][j] = x
#             DistanceMatrix[j][i] = x

# for i in range(20):
#     for j in range(20):
#         if i > j:
#             x = (TimeMatrix[i][j] + TimeMatrix[j][i]) / 2
#             x = float("{0:.2f}".format(x))
#             TimeMatrix[i][j] = x
#             TimeMatrix[j][i] = x
#
# for rows in TimeMatrix:
#     print(rows)





#Code for sprting pickup points according to their angles from the vertical
long1=float(coordinates[0][1])
lat1=float(coordinates[0][0])
newAngles=[]

for coordinate in coordinates:
    long2=float(coordinate[1])
    lat2=float(coordinate[0])
    dLon = (long2 - long1)

    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1)* math.cos(lat2) * math.cos(dLon);

    brng = math.atan2(y, x)

    brng = math.degrees(brng)
    brng = (brng + 360) % 360

    newAngles.append(brng)


sortedAngles=newAngles.copy()
sortedAngles.sort()

sortedPlaces=[]
for x in sortedAngles:
    sortedPlaces.append(places[newAngles.index(x)])

for angle in sortedAngles:
    index=newAngles.index(angle)
    print(places[index])




#===========================================================================
#Initial Route Generation Phase
#===========================================================================

#List of passengers at each PickUp point(pickup points are in order of sorted angles)
passengers = [0, 6, 5, 4, 5, 6, 4, 5, 4, 5, 4, 4, 6, 5, 4, 6, 6, 4, 4, 5]


#initial solution with no 85% capacity constraint
capRoutes=[]

sum=0
route=[]
route.append(places[0])
temp=1
occupancyList=[]

for i in range(1,len(places)):
    if temp<=minBuses-1:
        if occupancy>=sum>=minOccupancy:
            route.append(places[0])
            r=route.copy()
            capRoutes.append(r)
            occupancyList.append(sum)
            route.clear()
            route.append(places[0])
            sum=0
            sum+=passengers[i]
            temp+=1

            route.append(places[newAngles.index(sortedAngles[i])])
        else:
            sum+=passengers[i]
            route.append(places[newAngles.index(sortedAngles[i])])
    else:
        sum+=passengers[i]
        route.append(places[newAngles.index(sortedAngles[i])])

route.append(places[0])
capRoutes.append(route)
occupancyList.append(sum)

print("Initial Solution with no 85% capacity constraint:")
print(capRoutes)


#occupancy list contains
for i in range(len(occupancyList)):
    occupancyList[i]-=minOccupancy


print(occupancyList)

upperBound=occupancy-minOccupancy
lowerBound=0

def swap(everyRoute,ind,node1,node2):
    intermediateRoute = []
    route1=everyRoute[ind].copy()
    route1[route1.index(node1)]=node2
    route2=everyRoute[-1].copy()
    route2[route2.index(node2)]=node1
    for i in range(len(everyRoute)-1):
        if i!=ind:
            intermediateRoute.append(everyRoute[i].copy())
        else:
            intermediateRoute.append(route1)
    intermediateRoute.append(route2)

    intermediateOccupancies=[]

    for route in intermediateRoute:
        sum=0
        for x in route:
            sum+=passengers[sortedPlaces.index(x)]
        intermediateOccupancies.append(sum-28)

    print(intermediateOccupancies)
    print(intermediateRoute)
    return  intermediateRoute,intermediateOccupancies







allPossibleRoutes=[]
allPossibleOccupancy=[]

lastRoute=capRoutes[-1]
if occupancyList[-1]>upperBound:
    for route in capRoutes[0:-1]:
        for node_l in lastRoute[1:-1]:
            temp_l=passengers[sortedPlaces.index(node_l)]
            for node in route[1:-1]:
                temp=passengers[sortedPlaces.index(node)]
                if (occupancyList[-1]-upperBound)<=(temp_l-temp)<=(upperBound-occupancyList[capRoutes.index(route)]):
                    newRoute,newOccupancies=swap(capRoutes,capRoutes.index(route),node,node_l)
                    allPossibleRoutes.append(newRoute)
                    allPossibleOccupancy.append(newOccupancies)
elif occupancyList[-1]<lowerBound:
    for route in capRoutes[0:-1]:
        for node_l in lastRoute[1:-1]:
            temp_l=passengers[sortedPlaces.index(node_l)]
            for node in route[1:-1]:
                temp=passengers[sortedPlaces.index(node)]
                if (lowerBound-occupancyList[-1])<=(temp-temp_l)<=(occupancyList[capRoutes.index(route)]):
                    newRoute,newOccupancies=swap(capRoutes,capRoutes.index(route),node,node_l)
                    allPossibleRoutes.append(newRoute)
                    allPossibleOccupancy.append(newOccupancies)
else:
    allPossibleRoutes.append(capRoutes)

allPossibleRouteTime=[]

for routes in allPossibleRoutes:
    route_time=[]
    for route in routes:
        cost=0
        for i in range(len(route)-1):
            cost+=TimeMatrix[places.index(route[i])][places.index(route[i+1])]
        route_time.append(cost)
    allPossibleRouteTime.append(route_time)



allPossibleRouteCosts=[]

for routes in allPossibleRoutes:
    route_cost=[]
    for route in routes:
        cost=0
        for i in range(len(route)-1):
            cost+=DistanceMatrix[places.index(route[i])][places.index(route[i+1])]
        route_cost.append(cost)
    allPossibleRouteCosts.append(route_cost)
print("\nDistance costs:")
for costs in allPossibleRouteCosts:
    print(costs)
print("\nTime costs:")
for costs in allPossibleRouteTime:
    print(costs)



# NEIGHBORHOOD SOLUTIONS

def find_neighborhood(solution):
    """
    Pure implementation of generating the neighborhood (sorted by total distance of each solution from
    lowest to highest) of a solution with 1-1 exchange method, that means we exchange each node in a solution with each
    other node and generating a number of solution named neighborhood.
    :param solution: The solution in which we want to find the neighborhood.
    :param dict_of_neighbours: Dictionary with key each node and value a list of lists with the neighbors of the node
    and the cost (distance) for each neighbor.
    :return neighborhood_of_solution: A list that includes the solutions and the total distance of each solution
    (in form of list) that are produced with 1-1 exchange from the solution that the method took as an input
    Example:
    >>) find_neighborhood(['a','c','b','d','e','a'])
    [['a','e','b','d','c','a',90], [['a','c','d','b','e','a',90],['a','d','b','c','e','a',93],
    ['a','c','b','e','d','a',102], ['a','c','e','d','b','a',113], ['a','b','c','d','e','a',93]]
    """

    neighborhood_of_solution = []

    for n in solution[1:-1]:
        idx1 = solution.index(n)
        for kn in solution[1:-1]:
            idx2 = solution.index(kn)
            if n == kn:
                continue

            _tmp = copy.deepcopy(solution)
            _tmp[idx1] = kn
            _tmp[idx2] = n

            costDistance = 0

            for k in _tmp[:-1]:
                next_node = _tmp[_tmp.index(k) + 1]
                costDistance=costDistance+DistanceMatrix[places.index(k)][places.index(next_node)]
            _tmp.append(costDistance)

            if _tmp not in neighborhood_of_solution:
                neighborhood_of_solution.append(_tmp)

    indexOfLastItemInTheList = len(neighborhood_of_solution[0]) - 1

    neighborhood_of_solution.sort(key=lambda x: x[indexOfLastItemInTheList])
    return neighborhood_of_solution



# #TABU SEARCH


def tabu_search(
    first_solution, distance_of_first_solution, iters, size
):
    """
    Pure implementation of Tabu search algorithm for a Travelling Salesman Problem in Python.
    :param first_solution: The solution for the first iteration of Tabu search using the redundant resolution strategy
    in a list.
    :param distance_of_first_solution: The total distance that Travelling Salesman will travel, if he follows the path
    in first_solution.
    :param dict_of_neighbours: Dictionary with key each node and value a list of lists with the neighbors of the node
    and the cost (distance) for each neighbor.
    :param iters: The number of iterations that Tabu search will execute.
    :param size: The size of Tabu List.
    :return best_solution_ever: The solution with the lowest distance that occured during the execution of Tabu search.
    :return best_cost: The total distance that Travelling Salesman will travel, if he follows the path in best_solution
    ever.
    """
    #print(first_solution)
    count = 1
    solution = first_solution
    tabu_list = list()
    best_cost = distance_of_first_solution
    best_solution_ever = solution

    while count <= iters:
        neighborhood = find_neighborhood(solution)
        #print(neighborhood)
        index_of_best_solution = 0
        best_solution = neighborhood[index_of_best_solution]
        best_cost_index = len(best_solution) - 1

        found = False
        while found is False:
            i = 0
            while i < len(best_solution):

                if best_solution[i] != solution[i]:
                    first_exchange_node = best_solution[i]
                    second_exchange_node = solution[i]
                    break
                i = i + 1

            if [first_exchange_node, second_exchange_node] not in tabu_list and [
                second_exchange_node,
                first_exchange_node,
            ] not in tabu_list:
                tabu_list.append([first_exchange_node, second_exchange_node])
                found = True
                solution = best_solution[:-1]
                cost = neighborhood[index_of_best_solution][best_cost_index]
                if cost < best_cost:
                    best_cost = cost
                    best_solution_ever = solution
            else:
                index_of_best_solution = index_of_best_solution + 1
                #print(index_of_best_solution)
                best_solution = neighborhood[index_of_best_solution]

        if len(tabu_list) >= size:
            tabu_list.pop(0)

        count = count + 1

    return best_solution_ever, best_cost


allInitialCosts=[]

for routes in allPossibleRoutes:
    initialCosts=[]
    for i in range(len(routes)):
        cost=0
        for k in routes[i][:-1]:
            next_node = routes[i][routes[i].index(k) + 1]
            cost = cost + DistanceMatrix[places.index(k)][places.index(next_node)]
        initialCosts.append(cost)
    allInitialCosts.append(initialCosts)



allBestPossible=[]
allBestCosts=[]

for k in range(len(allPossibleRoutes)):
        bestSolutions=[]
        bestCosts=[]
        for j in range(len(allPossibleRoutes[k])):
            bestsol,bestCost=tabu_search(allPossibleRoutes[k][j],allInitialCosts[k][j],20,5)
            bestSolutions.append(bestsol)
            bestCosts.append(bestCost)

        allBestPossible.append(bestSolutions)
        allBestCosts.append(bestCosts)

print("\n")
for i in range(len(allBestCosts)):
    print(allBestPossible[i])
    print(allBestCosts[i])
    print("\n")


allTimes=[]
remove_routes=[]
remove_costs=[]
for routes in allBestPossible:
    route_time=[]
    for route in routes:
        cost=0
        for i in range(len(route)-1):
            cost+=TimeMatrix[places.index(route[i])][places.index(route[i+1])]
        route_time.append(cost)
        if cost>132.5:
            remove_routes.append(routes)
            remove_costs.append(allBestCosts[allBestPossible.index(routes)])
            break


for i in remove_routes:
    allBestPossible.remove(i)
for i in remove_costs:
    allBestCosts.remove(i)


for routes in allBestPossible:
    route_time=[]
    for route in routes:
        cost=0
        for i in range(len(route)-1):
            cost+=TimeMatrix[places.index(route[i])][places.index(route[i+1])]
        route_time.append(cost)
    allTimes.append(route_time)





for i in range(len(allBestCosts)):
    print(allBestPossible[i])
    print(allBestCosts[i])
    print(allTimes[i])

indexMin=0
minSum=0
for j in allBestCosts[0]:
    minSum+=j
for i in range(len(allBestPossible)):
    sum=0
    for j in allBestCosts[i]:
        sum+=j
    if sum<minSum:
        indexMin=i
        minSum=sum


print("FINAL SOLUTION:")
print(allBestPossible[indexMin])
print("Cost:")
print(minSum)


