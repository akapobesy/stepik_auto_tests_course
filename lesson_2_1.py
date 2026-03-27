from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_radio = browser.find_element(By.ID, "treasure")
    treasure_checked = treasure_radio.get_attribute("valuex")
    answer = calc(treasure_checked)
    buttom = browser.find_element(By.ID, "answer")
    buttom.send_keys(answer)
    buttom1 = browser.find_element(By.ID, "robotCheckbox").click()
    buttom2 = browser.find_element(By.ID, "robotsRule")
    buttom2.click()
    buttom3 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    buttom3.click()
          

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()