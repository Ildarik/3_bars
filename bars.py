import json
import os
from sys import argv
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    earth_radius = 6371
    return c * earth_radius


def load_data(filepath):
    if not os.path.exists(filepath):
    	return None
    with open(filepath, encoding = "Windows-1251") as file_handler:
    	return json.load(file_handler)


def get_biggest_bar(data):
    bars_dict = {}
    for bar in data:
        bars_dict.update({bar['Name']: bar['SeatsCount']})
    biggest_bar = max(bars_dict, key=bars_dict.get)
    return biggest_bar

def get_smallest_bar(data):
    bars_dict = {}
    for bar in data:
        bars_dict.update({bar['Name']: bar['SeatsCount']})
    smallest_bar = min(bars_dict, key=bars_dict.get)
    return smallest_bar

def get_closest_bar(data, longitude, latitude):
    bars_dict = {}
    for bar in data:
        lon2 = bar['geoData']['coordinates'][0]
        lat2 = bar['geoData']['coordinates'][1]
        distance_to_bar = haversine(longitude, latitude, lon2, lat2)
        bars_dict.update({bar['Name']: distance_to_bar})
    closest_bar_name = min(bars_dict, key=bars_dict.get)
    return closest_bar_name


def handle_user_input(description):
    try:
        user_input = float(input('Введите {}: '.format(description)))
    except ValueError:
        user_input = None
    return user_input


if __name__ == '__main__':
    our_json = load_data(argv[1])
    print('Самый большой бар: ', get_biggest_bar(our_json))
    print('Самый маленький бар: ', get_smallest_bar(our_json))
    
    longitude = handle_user_input('широта')
    latitude = handle_user_input('долгота')

    print('Самый близкий бар: ', get_closest_bar(our_json, longitude, latitude))