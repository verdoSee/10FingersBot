from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random

answer = input("Do you want to sign in to 10fingers? [y]/[n]: ")
if (answer == 'y'):
    Uemail = input("Email: ")
    sleep(0.5)
    Upasswd = input("Password: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path = PATH, options=options)
driver.get("https://10fastfingers.com/typing-test/english")
sleep(2)
search = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

if  (answer == 'y'):
    login = driver.find_element_by_xpath('/html/body/div[3]/div/nav/div[2]/ul[4]/li[2]/a').click()
    sleep(1)
    email = driver.find_element_by_id("UserEmail")
    email.send_keys(Uemail)
    passwd = driver.find_element_by_id("UserPassword")
    passwd.send_keys(Upasswd)
    loginButton = driver.find_element_by_xpath('//*[@id="login-form-submit"]').click()
sleep(3)

try: 
    list = driver.find_element_by_id("wordlist")
    input = driver.find_element_by_id("inputfield")
    string = ""

    for word in list.get_attribute('innerHTML'):
        string += word

    string = string.replace(" ","")
    string = string.replace("|", " ")
    Time = driver.find_element_by_id('timer')
    timer = ""
    
    for words in string.split():
        if (timer != "0:00"):
            input.send_keys(words)
            input.send_keys(Keys.SPACE)
            timer = Time.get_attribute('innerHTML')
            sleep(0)
except NoSuchElementException:
    print("WRONG PASSWORD OR EMAIL")


