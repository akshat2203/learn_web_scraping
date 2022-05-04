import time
import requests
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
import pandas as pd

# linkedin post data scrap using selenium and BeautifulSoup

# driver = webdriver.Chrome("./chromedriver")
#
# driver.get("https://linkedin.com/uas/login")
#
# username = driver.find_element_by_id("username")
# username.send_keys("username")
# pword = driver.find_element_by_id("password")
# pword.send_keys("password")
#
# driver.find_element_by_xpath("//button[@type='submit']").click()
#
# time.sleep(5)
#
#
# src = driver.page_source
#
# soup = BeautifulSoup(src, 'lxml')
# intro = soup.find_all('div', {'class': 'relative'})
#
# print(intro)


# page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
#
# soup = BeautifulSoup(page.content, 'html.parser')
#
# print(soup.prettify())
#
# page_children = list(soup.children)
# print(page_children)


# scrap 25 Machine Learning projects idea using BeautifulSoup

url = "https://www.interviewbit.com/blog/machine-learning-projects/"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
print(soup.title)

project_list = []

for link in soup.find_all('h4'):
    project_list.append({"title": link.text, "details": link.find_next('p').find_next('p').find_next('p').text})

print(project_list[6])
print(len(project_list))


# four type of objects

# tag object
soup = BeautifulSoup('<b class="boldest">Test</b>')
tag = soup.html
print(tag.name)
print(type(tag))
print(soup.b['class'])

# NavigableString object
soup = BeautifulSoup("<h2 id='message'>Hello, this is test</h2>")
print(soup)
print(soup.string)
print(type(soup.string))

# BeautifulSoup object
soup = BeautifulSoup("<h2 id='message'>Hello, Test</h2>")
print(type(soup))
print(soup.name)

# Comments object
soup = BeautifulSoup('<p><!-- Everything inside it is COMMENTS --></p>')
comment = soup.p.string
print(type(comment))
print(type(comment))
print(soup.p.prettify())

# siblings methods
# find_next_siblings(name, attrs, string, limit, **kwargs)
# find_next_sibling(name, attrs, string, **kwargs)
#
# find_previous_siblings(name, attrs, string, limit, **kwargs)
# find_previous_sibling(name, attrs, string, **kwargs)
#
# find_all_next(name, attrs, string, limit, **kwargs)
# find_next(name, attrs, string, **kwargs)
#
# find_all_previous(name, attrs, string, limit, **kwargs)
# find_previous(name, attrs, string, **kwargs)


# encoding method for string
soup = BeautifulSoup("<h2>Hello, this is test</h2>")
print(soup)
print(soup.string)
print(soup.original_encoding)
print(type(soup.string))

# Only "a" tags
only_a_tags = SoupStrainer("a")

# Will parse only the below mentioned "ids".
parse_only = SoupStrainer(id=["first", "third", "my_unique_id"])
soup = BeautifulSoup(my_document, "html.parser", parse_only=parse_only)


# parse only where string length is less than 10
def is_short_string(string):
    return len(string) < 10


only_short_strings = SoupStrainer(string=is_short_string)

# encoding method for string

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)


img = tonight.find("img")
desc = img['title']
print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)

# data in pandas frame

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})

print(weather)

temp_nums = weather["temp"].str.extract("(?Pd+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')

print(temp_nums)

weather["temp_num"].mean()
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night

print(is_night)
print(weather[is_night])
