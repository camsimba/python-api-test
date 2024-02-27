import requests 
from PIL import Image 
from html2image import Html2Image

API_KEY = 'BM6A8mdPSJe7jAq4w4He4GX5ttAVgeKRPcoMsrey'

def APOD():
    params = {"api_key": API_KEY}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    res = response.json()
    print(res['explanation'])
    img_url = res['hdurl']
    im = Image.open(requests.get(img_url, stream=True).raw)
    im.show()

def mars_weather():
    params = {'api_key': API_KEY}
    response = requests.get('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')
    res = response.json()
    if len(res['sol_keys']) == 0:
        print('No recent data available')
    else: return res

    #Display weather report images
    hti = Html2Image()
    hti.screenshot(url='https://mars.nasa.gov/layout/embed/image/insightweather/', save_as='insight_weather.png')
    im_i = Image.open('insight_weather.png')
    im_i = im_i.crop((0,0,1920,680))

    hti.screenshot(url='https://mars.nasa.gov/layout/embed/image/mslweather/', save_as='curiosity_weather.png')
    im_c = Image.open('curiosity_weather.png')
    im_c = im_c.crop((0, 0, 1920, 680))

    im = Image.new('RGB',size=(1920,1360))
    im.paste(im_i, (0,0))
    im.paste(im_c, (0, 675))
    im.show()