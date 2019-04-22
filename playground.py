from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os




driver = webdriver.Firefox(executable_path='bins/geckodriver')
driver.get('https://www.indeed.com')
assert 'Job Search | Indeed ' == driver.title, driver.title