import requests

API_KEY ="51793b2251ba7e9417dbbb8519c7b903"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_Data = data["list"]
    nr_values = 8 * forecast_days
    filtered_Data = filtered_Data[:nr_values]

    return filtered_Data

if __name__ == "__main__":
    print(get_data(place="Santo Domingo, DO", forecast_days=1))