import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

service=webdriver.chrome.service.Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()

"""
# Samsung Lions Go!!


"""

url='https://m.sports.naver.com/game/20240604SSSK02024'
driver.get(url)
