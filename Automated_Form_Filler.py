from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.binary_location = '/usr/bin/chromium'
driver = webdriver.Chrome("D:\Python files\Web Automation\chromedriver.exe")


info = {'Name': 'Agusto Belmonte', 'email': 'agusto.belmonte@gmail.com',
        'Phone': '1234567890', 'Country': 'India', 'City': 'Pune'
        , 'State': 'Maharashtra'}

test_website_link = 'https://docs.google.com/forms/d/e/1FAIpQLSe5-ppmNgHVrixc1nk_U1CKdkLvqtPusSckg12DzdQRCuVVmw/viewform'
driver.get(test_website_link)

## For Name
try:
    field_name = driver.find_element_by_xpath("//input[@type='text']")
    field_name.send_keys(info['Name'])
except:
    print("No 'name' field found\n")

time.sleep(1)

## For email
try:
    field_email = driver.find_element_by_xpath("//input[@type='email']")
    field_email.send_keys(info['email'])
except:
    print("No 'email' field found\n")

time.sleep(1)


## For Phone No.
try:
    field_num = driver.find_element_by_xpath('//input[@aria-label="Phone No."]')
    field_num.send_keys(info['Phone'])
except:
    print("No 'Phone No.' field found\n")

time.sleep(1)


## For Country
try:
    field_country = driver.find_element_by_xpath('//input[@aria-label="Country"]')
    field_country.send_keys(info['Country'])
except:
    print("No 'Country' field found\n")

time.sleep(1)


## For State
try:
    field_state = driver.find_element_by_xpath('//input[@aria-label="State"]')
    field_state.send_keys(info['State'])
except:
    print("No 'State' field found\n")

time.sleep(1)


## For City
try:
    field_city = driver.find_element_by_xpath('//input[@aria-label="City"]')
    field_city.send_keys(info['City'])
except:
    print("No 'City' field found\n")

time.sleep(1)


## Submitting the form
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div[1]/div').click()

time.sleep(1)

## Close the Driver
driver.close()
