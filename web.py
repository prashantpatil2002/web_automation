
import time
from selenium import webdriver
import selenium 
path = r"C:\Users\prash\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.google.com")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("ethical hacking")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]').click()
time.sleep(6)
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[5]/a').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3').click()
 


