import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('http://127.0.0.1:5000')
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