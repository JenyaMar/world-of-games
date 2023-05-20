import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def scores_service():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)
    driver.get('http://127.0.0.1:5000')
    time.sleep(5)
    score = driver.find_element(By.ID, 'score')
    return True if (int(score.text) >= 1 and int(score.text) <= 1000) else False

def main_function():
    result = scores_service()
    if result:
        sys.exit(0)
    else:
        sys.exit(1)

main_function()
