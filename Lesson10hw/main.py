import sqlite3
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_temperature():
    url = "https://sinoptik.ua/Погода у Києві"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    temperature = soup.find(class_="temperature").get_text().strip()
    return temperature

def insert_data(date_time, temperature):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("INSERT INTO WeatherInKyiv (date_time, temperature) VALUES (?, ?)", (date_time, temperature))
    conn.commit()
    conn.close()

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

temperature = get_temperature()

insert_data(current_datetime, temperature)

print("Success , check data-base.")