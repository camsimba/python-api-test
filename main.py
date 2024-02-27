import nasa_api as nasa
from tabulate import tabulate

api_info = [
    ['Index', 'Endpoint', 'Desc'],
    [0, 'APOD', 'Returns the Astronomy Picture of the Day'],
    [1, 'InSight', 'Returns data + info panel of Martian weather'],
]

def main():
    print(tabulate(api_info))
    cmd = input("Which API would you like to call?\n")
    try:
        selector(cmd)
    except:
        print("Typed API does not exist, please enter a valid API name.")
        main()
    

def selector(api_name):
    func = getattr(nasa, api_name)
    func()


main()