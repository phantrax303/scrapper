from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# specify the url
urlpage = 'https://www.instagram.com/' 

options = webdriver.ChromeOptions()
options.headless = True

# run firefox webdriver from executable path of your choice
driver = webdriver.Chrome(executable_path = r'C:/Users/gabriel.sales/Downloads/scrapper/chromedriver.exe')

# get web page
driver.get(urlpage)
# execute script to scroll down the page
try: 
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"username")))
finally:
    email = driver.find_element(By.NAME,"username")
    email.send_keys('phantrax202@gmail.com')
    password = driver.find_element(By.NAME,"password")
    password.send_keys('Ks@les303')
    password.submit()
   
    #driver.execute_script("email = document.getElementById('email').setAttribute('value','phantrax202@gmail.com');"+
    #                "pass = document.getElementById('pass').setAttribute('value','Ks@les303');"+
    #                "document.getElementsByTagName('Form')[0].submit()")
try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"XrOey")))
finally:
    img = driver.find_element(By.XPATH,'//div[@class="XrOey"]/div').click()
    print(img)

# find elements by xpath
#results = driver.find_elements_by_xpath("//*[@class=' co-product-list__main-cntr']//*[@class=' co-item ']//*[@class='co-product']//*[@class='co-item__title-container']//*[@class='co-product__title'
time.sleep(3000)
# driver.quit()

def login():
    pass