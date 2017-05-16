import json
import os
from sys import argv
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def load_data(filepath):
    # output_file = open(filepath, encoding = "Windows-1251").read()
    # output_json = json.loads(output_file)
    # return output_json

    if not os.path.exists(filepath):
    	return None
    with open(filepath, encoding = "Windows-1251") as file_handler:
    	return json.load(file_handler) 

def get_biggest_bar(data):
    BiggestBarSeatsCount = 0
    BiggestBarName = ''
    for bar in data:
    	if bar['SeatsCount'] > BiggestBarSeatsCount:
    		BiggestBarSeatsCount = bar['SeatsCount']
    		BiggestBarName = bar['Name']
    return BiggestBarName


def get_smallest_bar(data):
    SmallestBarSeatsCount = 1000
    SmallestBarName = ''
    for bar in data:
    	if bar['SeatsCount'] < SmallestBarSeatsCount:
    		SmallestBarSeatsCount = bar['SeatsCount']
    		SmallestBarName = bar['Name']
    return SmallestBarName


def get_closest_bar(data, longitude, latitude):
    distance = 1000
    ClosestBarName = ''
    for bar in data:
        lon2 = bar['geoData']['coordinates'][0]
        lat2 = bar['geoData']['coordinates'][1]
        DistanceToBar = haversine(longitude, latitude, lon2, lat2)        
        if DistanceToBar < distance:
            distance = DistanceToBar
            ClosestBarName = bar['Name']
    return ClosestBarName


if __name__ == '__main__':
    our_json = load_data(argv[1])
    print('Самый большой бар: ', get_biggest_bar(our_json))
    print('Самый маленький бар: ', get_smallest_bar(our_json))
    
    try:
        longitude = float(input('Введите широту: '))
    except ValueError:
        longitude = None

    try:
        latitude = float(input('Введите долготу: '))
    except ValueError:
        latitude = None

    print('Самый близкий бар: ', get_closest_bar(our_json, longitude, latitude))