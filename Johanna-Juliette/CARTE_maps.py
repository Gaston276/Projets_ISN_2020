# -*- coding: utf-8 -*-

import googlemaps
from datetime import datetime

gmaps =googlemaps.Client('AIzaSyAvS38oDMKMfzaVXhM8GOnpjEl047DiKVM')

cities = ["Strasbourg","Nancy"]

now = datetime.now()
directions_result = gmaps.directions("18.997739, 72.841280",
                                     "18.880253, 72.945137",
                                     mode="driving",
                                     avoid="ferries"
                                    )

print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])