from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class RadioButton:

    
    def __init__(self, url = "https://www.instagram.com/guviofficial/"):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def boot(self):
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()
       sleep(10)


    def clickfollowers(self, followers):
       #absoluteXpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a"
       #absoluteXpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button/span"
       titles = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button/span')
       print(titles[0].get_attribute('title'))
       #element = self.driver.find_element(by=By.XPATH, value=absoluteXpath)
       #element.send_keys(followers)
       sleep(5)
       
    def clickfollowing(self,following):
       absoluteXpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[3]/div/button"
       element = self.driver.find_element(by=By.XPATH, value=absoluteXpath)
       element.send_keys(followers)
       sleep(5)
      
obj1=RadioButton()
print(obj1.clickfollowers)
print(obj1.clickfollowing)