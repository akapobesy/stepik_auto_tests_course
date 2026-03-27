from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "https://suninjuly.github.io/math.html?ruler=robots"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = button.text
    answer = calc(x)
    button1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    button1.send_keys(answer)
    button2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button2.click()
    button3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button3.click()
    button5 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button5.click()
   

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()