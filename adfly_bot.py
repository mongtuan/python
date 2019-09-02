#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


firef = webdriver.Firefox()
firef.get('http://thacorag.com/2Lwk')
element = WebDriverWait(firef, 20).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/table/tbody/tr[1]/td/div/div[1]/span[2]/a/img")))

element.click();
