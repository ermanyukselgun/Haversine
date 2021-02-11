# d : Distance between two points in kilometers
# r : Radius of the earth which is 6371 km
# ϕ (phi) : latitude
# λ (lambda) : longtitude

# You are given list of dictionaries which represents several capitals in worldwide, each dictionary has three different
# keys which are name, lat for latitude and lon for longtitude values.

# Haversine Formula – Calculate geographic distance on earth.
# If you have two different latitude – longitude values of two different point on earth,
# then with the help of Haversine Formula, you can easily compute the great-circle distance
# (The shortest distance between two points on the surface of a Sphere).
# This is not the exact measurement because
# the formula assumes that the Earth is a perfect sphere when in fact it is an oblate spheroid.

# TASK 1
# You have to create haversine function that takes two parameters which are two points on the earth and calculates
# distance between each other and finally returns this distance as an integer value,
# Latitude and longitude need to be in radians for calculation.
# haversine formula provided you inside of .zip file as an image.

# TASK 2
# You have to create table_data function that takes one parameter (cities list) and returns two different values
# which are the list consist of name of the cities, the second return value is two dimensional list that consist of
# distances between each city respectively

from math import radians, sin, cos, asin, sqrt

# These are the math module methods that you can use
# math.radians()
# math.sin()
# math.cos()
# math.asin()
# math.sqrt()
# pow()

cities = [{"name": "Buenos Aires", "lat": -34.58333333, "lon": -58.666667},
          {"name": "Vienna", "lat": 48.2, "lon": 16.366667},
          {"name": "Baku", "lat": 40.38333333, "lon": 49.866667},
          {"name": "Beijing", "lat": 39.91666667, "lon": 116.383333},
          {"name": "Paris", "lat": 48.86666667, "lon": 2.333333},
          {"name": "Berlin", "lat": 52.51666667, "lon": 13.4},
          {"name": "Dublin", "lat": 53.31666667, "lon": -6.233333},
          {"name": "Mexico City	", "lat": 19.43333333, "lon": -99.133333},
          {"name": "Lisbon", "lat": 38.71666667, "lon": -9.133333},
          {"name": "Washington", "lat": 38.883333, "lon": -77},
          {"name": "Ankara", "lat": 39.93333333, "lon": 32.866667},
          ]


def haversine(departure, arrival):
    r = 6371 # r : Radius of the earth which is 6371 km
     # convert decimal degrees to radians

    for i in range(len(cities)):
        if cities[i]["name"]==departure:
            departure_index=i
            break
    for i in range(len(cities)):
        if cities[i]["name"]==arrival:
            arrival_index=i
            break
    lon1 = cities[departure_index]["lon"] 
    lat1 = cities[departure_index]["lat"]
    lon2 = cities[arrival_index]["lon"]
    lat2 = cities[arrival_index]["lat"]
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    #haversine formula
    dlon =lon2-lon1
    dlat = lat2-lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    return c * r

    # returns the distance between two points in kilometers and data type is integer





def table_data(cities):    
    # returns two different values which are :
    # cities(list of the name of the cities) and
    # distance_data(distance of each city with the rest of the cities) i.e.
    # [
    # ['0', '11824', '13849', '19278', '11063', '11923', '11001', '7373', '9612', '8384', '12499'],
    # ['11824', '0', '2778', '7459', '1034', '523', '1679', '10151', '2297', '7122', '1601'],
    # .
    # .
    # ['12499', '1601', '1443', '6830', '2599', '2037', '3281', '11751', '3581', '8724', '0']
    # ]
    distance_data=[]
    for i in range(len(cities)):
        temp = []
        name_of_cities= cities[i]["name"]
        for j in range(len(cities)):
            temp.append((str(int(haversine(name_of_cities,cities[j]["name"])))))
        distance_data.insert(i,temp)
    name_of_cities = []
    for i in range(len(cities)):
        name_of_cities.append(cities[i]["name"])
    return name_of_cities, distance_data


# DO NOT CHANGE THIS METHOD
# This method will print your data in tabular format to console.
def print_table(cities, distance_data):
    row_format = "{:15}" * (len(cities) + 1)
    print(row_format.format("", *cities))
    for city, row in zip(cities, distance_data):
        print(row_format.format(city, *row))


# These two lines required entry point of your program, code execution will be started from here
name_of_cities, distance_data = table_data(cities)
print_table(name_of_cities, distance_data)


