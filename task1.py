import requests
from bs4 import BeautifulSoup
import pandas as pd

request_url = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(request_url.content, 'html.parser')

all_days = soup.find(id="seven-day-forecast")
period_data = all_days.select(".tombstone-container .period-name")

periods = []
for data in period_data:
    periods.append(data.get_text())
print(periods)

short_desc = []
for data in all_days.select(".tombstone-container .short-desc"):
    short_desc.append(data.get_text())
print(short_desc)

temps = []
for data in all_days.select(".tombstone-container .temp"):
    temps.append(data.get_text())
print(temps)

desc = []
for data in all_days.select(".tombstone-container img"):
    desc.append(data.get('title'))
print(desc)

weather_data = pd.DataFrame({
    "desc": desc,
    "period": periods,
    "short_desc": short_desc,
    "temp": temps
})
print(weather_data)
print(weather_data["temp"])

temp_nums = weather_data["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather_data["temp_num"] = temp_nums.astype('int')
weather_data["temp_num"].mean()

is_night = weather_data["temp"].str.contains("Low")
weather_data["is_night"] = is_night

weather_data.to_csv('weather_data.csv', index=False)
