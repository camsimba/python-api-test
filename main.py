

import requests 
from PIL import Image 


API_KEY = 'BM6A8mdPSJe7jAq4w4He4GX5ttAVgeKRPcoMsrey'

def APOD():
    params = {"api_key": API_KEY}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    res = response.json()
    print(res['explanation'])
    img_url = res['hdurl']
    im = Image.open(requests.get(img_url, stream=True).raw)
    im.show()

APOD()

