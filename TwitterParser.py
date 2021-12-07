from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://twitter.com/elonmusk')
    action = ActionChains(driver)

    sleep(2)
    timeline = driver.find_element(By.XPATH, '//div[@aria-label="Timeline: Elon Musk’s Tweets"]/div')

    unique_posts = {}
    number_of_posts_to_get = 10
    while len(unique_posts) < number_of_posts_to_get:
        posts = timeline.find_elements(By.XPATH, './/div[@lang]')
        unique_posts.update(dict.fromkeys([x.text for x in posts]))
        action.move_to_element(posts[-1])
        action.perform()

    for post in list(unique_posts)[:number_of_posts_to_get]:
        print(post)
