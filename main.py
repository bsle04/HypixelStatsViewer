from gevent import monkey
monkey.patch_all(thread=False, select=False)

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import hypixel
import sys
sys.setrecursionlimit(2000)

#Webscrape function
def hypixelScrape():
    username = input('Enter a Hypixel username: ')
    # op = webdriver.ChromeOptions()
    # op.add_argument('headless')
    # driver = webdriver.Chrome(options=op)
    driver = webdriver.Chrome()
    driver.get("https://plancke.io/")

    inputElement=driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/form/div/input')
    inputElement.send_keys(username)

    inputElement = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/form/div/span/button')
    inputElement.click()

    inputElement = driver.find_element(By.XPATH, '//*[@id="stat_panel_BedWars"]/div[1]')
    inputElement.click()

    inputElement = driver.find_element(By.XPATH, '//*[@id="stat_panel_BedWars"]/div[1]')
    inputElement.click()

    element = driver.find_element(By.XPATH, '//*[@id="collapse-1-2"]/div/table/tbody/tr[23]/td[6]')
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="collapse-1-2"]/div/table/tbody/tr[23]/td[6]')))
    fkdr = element.text
    driver.quit()

    print(username + "'s Bedwars FKDR: " + fkdr)

#First pass at using hypixelpy, I believe it is outdated as some of its api calls are deprecated.
# def getBasicInfo():
#     API_KEYS = ['b8a3318c-d0f5-4dcf-b8c9-ecc8efbf4a55']
#     hypixel.setKeys(API_KEYS) # This sets the API keys that are going to be used.

#     Player = hypixel.Player('123shawty') # This creates a Player-object and puts it to a variable called "Player".

#     PlayerName = Player.getName() # This gets the player's name and puts it in a variable called "PlayerName". :3
#     print("Player is called ", end='')
#     print(PlayerName)

#     PlayerLevel = Player.getLevel()
#     print(PlayerName + " is level: ", end='')
#     print(PlayerLevel) # This prints the level that we got, two lines up!

#     PlayerRank = Player.getRank()
#     print(PlayerName + " is rank: ", end='')
#     print(PlayerRank['rank'])


if __name__ == '__main__':
    hypixelScrape()
