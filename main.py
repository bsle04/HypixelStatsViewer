from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def hypixel():
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

if __name__ == '__main__':
    hypixel()
