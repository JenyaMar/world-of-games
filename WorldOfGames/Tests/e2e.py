import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(url='http://127.0.0.1:5000'):
    ch_driver = webdriver.Chrome(
        executable_path='./chromedriver')
    ch_driver.get(url)
    score = ch_driver.find_element(By.ID, 'score')
    return True if (int(score.text) >= 1 and int(score.text) <= 1000) else False


def main_function():
    result = test_scores_service()
    if result:
        sys.exit(0)
    else:
        sys.exit(1)
