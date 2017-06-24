import json
import os
from sys import argv
from math import radians, cos, sin, asin, sqrt


def load_data(filepath):
    if not os.path.exists(filepath):
    	return None
    with open(filepath, encoding = "Windows-1251") as file_handler:
    	return json.load(file_handler)


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda bar: bar['SeatsCount'])
    biggest_bar_name = biggest_bar['Name']
    return biggest_bar_name


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda bar: bar['SeatsCount'])
    smallest_bar_name = smallest_bar['Name']
    return smallest_bar_name


def get_closest_bar(data, longitude, latitude):
    def haversine(bar, longitude=longitude, latitude=latitude):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        bar_longitude = bar['geoData']['coordinates'][0]
        bar_latitude = bar['geoData']['coordinates'][1]
        lon1, lat1, lon2, lat2 = map(radians, [longitude, latitude, bar_longitude, bar_latitude])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        earth_radius = 6371
        return c * earth_radius

    closest_bar = min(data, key=haversine)
    return closest_bar['Name']

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