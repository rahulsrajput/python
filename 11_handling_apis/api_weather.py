# tomorrow.io Site

import requests


def fetch_weather_data():
    base_url = 'https://api.tomorrow.io/v4/weather/realtime?'
    api_key = 'cSaupoyMCjOCX5valtKL88b1eDpYxUcF'

    location = input('Enter City Name: ')

    url = base_url + f'location={location}&apikey={api_key}'

    response = requests.get(url)
    print(type(response))

    data = response.json()
    print(type(data))
    # print(data)
    
    if "data" in data:
        weather_data = data["data"]
        time = weather_data["time"]
        temp = weather_data["values"]["temperature"]
        humidity = weather_data["values"]["humidity"]
        lat = data["location"]["lat"]
        lon = data["location"]["lon"]

        return time, temp, lat, lon, humidity
    

def main():
    try:
        time, temp, lat, lon, humidity = fetch_weather_data()
        print(f"Time:{time}\nTemp:{temp}\nHumidity:{humidity}\nLatitude:{lat}\nLongitutde:{lon}")
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()