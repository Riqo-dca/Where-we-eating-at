import requests
import random

def get_random_restaurant(location):
    api_key = 'Qngb16sRKvWfzzIuMhRCGra2nNWMbrbTyBUBmv1rcy3d68_6RTRyPm-KaZUItjhanQEfHV5YHtRupUvibqrzVsRXTzgGV9uTMFcyyL8YWyCzUIJCKyCVubXYUYHlZHYx'
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'location': location, 'term': 'restaurant', 'limit': 50}
    response = requests.get('https://api.yelp.com/v3/businesses/search', params=params, headers=headers)
    data = response.json()

    if 'businesses' in data:
        random_business = random.choice(data['businesses'])
        return random_business['name']
    else:
        return 'No restaurants found'
