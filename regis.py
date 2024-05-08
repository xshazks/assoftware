from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)

driver.get("https://google.com/")
driver.find_element(By.ID,"APjFqb").send_keys("tumblr")
time.sleep(2)

tombol = driver.find_element(By.CLASS_NAME,"gNO89b")
tombol.click()
time.sleep(2)

driver.get("https://www.tumblr.com/register")


driver.find_element(By.NAME,"email").send_keys("shahiezasauki@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Uki092515")
time.sleep(2)

tombol = driver.find_element(By.CLASS_NAME,"TRX6J.CxLjL.qjTo7.CguuB.yC5pj")
tombol.click()

driver.find_element(By.NAME,"month")
driver.find_element(By.NAME,"day").send_keys("1")
driver.find_element(By.NAME,"year").send_keys("2003")


tombol = driver.find_element(By.CLASS_NAME,"TRX6J.CxLjL.qjTo7.CguuB.yC5pj.E_Qq0")
tombol.click()

# tombol = driver.find_element_by_id ("month")
# tombol.select_by_index (1)
