# -*- coding: utf-8 -*-
import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "postal code": response.get("postal"),
        "region_code": response.get("region_code"),
        "country code": response.get("country"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }
    return location_data


print(get_location())