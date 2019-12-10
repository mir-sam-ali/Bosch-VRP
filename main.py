"""
Simple Program to help you get started with Google's APIs
"""
import urllib.request, json
import math

import utm

# Google MapsDdirections API endpoint
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

for place, coordinate in data['addresses'].items():
    places.append(place)
    coordinates.append(coordinate)
# print(len(places))
# print(len(coordinates))

for coordinate in coordinates:
    #print(coordinate[0],coordinate[1])
    utm_conversion = utm.from_latlon(float(coordinate[0]), float(coordinate[1]))
    l=utm_conversion[0:2]
    #print(l)
    UTM.append(l)

#print(UTM)


# for places, coordinate in data['addresses'].items():
#     row = []
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
#     # print(row)
#     DistanceMatrix.append(row)
#
# for i in range(20):
#     for j in range(20):
#         if i > j:
#             x = (DistanceMatrix[i][j] + DistanceMatrix[j][i]) / 2
#             x = float("{0:.2f}".format(x))
#             DistanceMatrix[i][j] = x
#             DistanceMatrix[j][i] = x

# for rows in DistanceMatrix:
#     print(rows)

# endpoint = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=17.385044,78.486671&destinations=19.075983,72.877655;12.971599,77.594566&travelMode=driving&key=AoRQLJZ4fFULwmeEEPFHMFVwAV5EAoPJ_r4EmLrPm2tDnpUgPQtzbSh5pcOx1Rg9"

# depot=list(UTM[0])
# newCoord=[]
#
# for cord in UTM:
#     x=cord[0]-depot[0]
#     y=cord[1]-depot[1]
#     l=[]
#     l.append(x)
#     l.append(y)
#     newCoord.append(l)
#
#
# origin=[0,0]
# angles=[]
# print(newCoord)
# for cord in newCoord:
#
#     if cord!=origin:
#         if cord[0]!=origin[0]:
#             slope=(cord[1]-origin[1])/(cord[0]-origin[0])
#             angle=math.atan(slope)
#             if cord[0] < 0 and cord[1] > 0:
#                 angle = math.pi + angle
#             elif cord[0] < 0 and cord[1] <= 0:
#                 angle = angle + math.pi
#             elif cord[0] > 0 and cord[1] < 0:
#                 angle = (angle) + math.pi * 2
#         else:
#             angle=math.pi/2
#             if(cord[1]<0):
#                 angle=math.pi*3/2
#
#         angles.append(angle)
#
#
# sortedAngles=angles.copy()
# sortedAngles.sort()
#
# highest=sortedAngles[len(sortedAngles)-1]
# lowest=sortedAngles[0]
# print(coordinates[angles.index(highest)])
# print(coordinates[angles.index(lowest)])
#
# print(sortedAngles)


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
print(sortedAngles)
#
for angle in sortedAngles:
    index=newAngles.index(angle)
    print(places[index])



allRoutes=[]
initialIndex=newAngles.index(sortedAngles[1])
distance=DistanceMatrix[0][initialIndex]
route=[]
route.append(places[0])

for i in range(1, 20):

    if i != 19:
        print("===========")
        print(sortedAngles[i])
        dist1Index=newAngles.index(sortedAngles[i])
        dist2Index=newAngles.index(sortedAngles[i+1])
        print(places[dist1Index])
        print(places[dist2Index])
        print("=============")
        distanceNextPoint=DistanceMatrix[dist1Index][dist2Index]
        distanceFromDepot=DistanceMatrix[dist2Index][0]
        print(distanceNextPoint)
        print(distanceFromDepot)
        print(distance)
        if (distance+distanceNextPoint+distanceFromDepot)<=92:
            distance+=distanceNextPoint
            print(places[dist1Index])
            route.append(places[dist1Index])
            print(route)

        else:
            print(places[dist1Index])
            route.append(places[dist1Index])
            route.append(places[0])
            print(route)
            print("######")
            oldRoute=route.copy()
            allRoutes.append(oldRoute)
            route.clear()
            route.append(places[0])
            distance=DistanceMatrix[0][dist2Index]
    else:
        print("lll")
        dist1Index = newAngles.index(sortedAngles[i])
        route.append(places[dist1Index])
        route.append(places[0])
        allRoutes.append(route)

print(allRoutes)

