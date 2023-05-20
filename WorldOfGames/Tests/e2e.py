import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service():
    driver = webdriver.Chrome('/chromedriver')
    driver.get('www.google.com')
    time.sleep(20)
    score = driver.find_element(By.ID, 'score')
    driver.quit()
    return True if (int(score.text) >= 1 and int(score.text) <= 1000) else False

def main_function():
    result = test_scores_service()
    if result:
        sys.exit(0)
    else:
        sys.exit(1)

main_function()
