import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_scores_service():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="/Users/jenyamartemyanov/Downloads/chromedriver_mac64/chromedriver.exe", options=chrome_options)
    driver.get('127.0.0.1:5000')
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
