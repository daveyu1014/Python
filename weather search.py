# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:20:23 2022

@author: dave7
"""

from bs4 import BeautifulSoup
import requests


headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
  "q": "Taipei weather",
  "hl": "en",
}

response = requests.get('https://www.google.com/search', headers=headers, params=params)
soup = BeautifulSoup(response.text, 'lxml')

location = soup.select_one('#wob_loc').text
weather_condition = soup.select_one('#wob_dc').text
tempature = soup.select_one('#wob_tm').text
precipitation = soup.select_one('#wob_pp').text
humidity = soup.select_one('#wob_hm').text
wind = soup.select_one('#wob_ws').text
current_time = soup.select_one('#wob_dts').text

print(f'Location: {location}\n'
      f'Weather condition: {weather_condition}\n'
      f'Temperature: {tempature}°F\n'
      f'Precipitation: {precipitation}\n'
      f'Humidity: {humidity}\n'
      f'Wind speed: {wind}\n'
      f'Current time: {current_time}\n')
