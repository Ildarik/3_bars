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
    earth_radius = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * earth_radius


def load_data(filepath):

    if not os.path.exists(filepath):
    	return None
    with open(filepath, encoding = "Windows-1251") as file_handler:
    	return json.load(file_handler) 

def get_biggest_bar(data):
    biggest_bar_seatscount = 0
    biggest_bar_name = ''
    for bar in data:
    	if bar['SeatsCount'] > biggest_bar_seatscount:
    		biggest_bar_seatscount = bar['SeatsCount']
    		biggest_bar_name = bar['Name']
    return biggest_bar_name


def get_smallest_bar(data):
    smallest_bar_seatscount = 1000
    smallest_bar_name = ''
    for bar in data:
    	if bar['SeatsCount'] < smallest_bar_seatscount:
    		smallest_bar_seatscount = bar['SeatsCount']
    		smallest_bar_name = bar['Name']
    return smallest_bar_name


def get_closest_bar(data, longitude, latitude):
    distance = 1000
    closest_bar_name = ''
    for bar in data:
        lon2 = bar['geoData']['coordinates'][0]
        lat2 = bar['geoData']['coordinates'][1]
        distance_to_bar = haversine(longitude, latitude, lon2, lat2)        
        if distance_to_bar < distance:
            distance = distance_to_bar
            closest_bar_name = bar['Name']
    return closest_bar_name


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