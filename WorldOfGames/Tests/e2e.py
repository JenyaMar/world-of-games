import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_scores_service(url='http://127.0.0.1:5000'):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Remote("http://127.0.0.1:5005/wd/hub", options=options, timeout=120)
    driver.get(url)
    score = driver.find_element(By.ID, 'score')
    return True if (int(score.text) >= 1 and int(score.text) <= 1000) else False

def main_function():
    result = test_scores_service()
    if result:
        sys.exit(0)
    else:
        sys.exit(1)

main_function()