from time import sleep
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.nseindia.com/')
    driver.delete_all_cookies()
    action = ActionChains(driver)

    # ------------------------------------Parsing------------------------------------
    main_navbar = driver.find_element(By.ID, 'main_navbar')

    market_data = main_navbar.find_element(By.XPATH, './/a[text()="Market Data"]')  # child of main_navbar
    # action.pause(1)
    action.move_to_element(market_data)
    # action.pause(1)

    pre_open_market = main_navbar.find_element(By.XPATH, './/a[text()="Pre-Open Market"]')  # child of market_data
    action.move_to_element(pre_open_market)
    # action.pause(1)
    action.click(pre_open_market)
    action.perform()

    # table: WebElement = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'table-preOpen')))
    # body: WebElement = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'tbody')))
    sleep(1)
    table = driver.find_element(By.ID, 'table-preOpen')
    body = table.find_element(By.TAG_NAME, 'tbody')
    rows = [r.split() for r in body.text.replace(',', '').splitlines()]

    with open('log.csv', mode='w', newline='') as log:
        csv.writer(log, delimiter=',').writerows(rows)

    # ------------------------------------User Activity------------------------------------
    sleep(0.5)
    driver.delete_all_cookies()
    main_button = driver.find_element(By.CLASS_NAME, 'navbar-brand.mr-auto')
    action.click(main_button)
    action.perform()

    sleep(0.5)
    driver.delete_all_cookies()
    graph = driver.find_element(By.ID, 'tab1_container')
    action.move_to_element(graph)
    action.click(driver.find_element(By.XPATH, '//*[@id="nse-indices"]/div[2]/div/div/nav/div/div/a[4]'))

    sleep(0.5)
    driver.delete_all_cookies()
    action.click(driver.find_element(By.XPATH, '//*[@id="gainers_loosers"]/div[3]/a'))
    action.perform()

    sleep(0.5)
    driver.delete_all_cookies()
    dropdown = Select(driver.find_element(By.ID, 'equitieStockSelect'))
    dropdown.select_by_value('NIFTY ALPHA 50')
    action.perform()

    # driver.close()
