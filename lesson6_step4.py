from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
import math
import pyperclip

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser,12).until(Ec.text_to_be_present_in_element((By.ID,'price'),'100'))
    button = browser.find_element(By.ID,'book')
    button.click()
    # Ваш код, который заполняет обязательные поля
    

    value = browser.find_element(By.ID,'input_value')
    field = browser.find_element(By.TAG_NAME,'input')
    field.send_keys(calc(value.text))
    
    submit = browser.find_element(By.ID,'solve')
    submit.click()

    answer = browser.switch_to.alert
    pyperclip.copy(answer.text.split()[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    
    # закрываем браузер после всех манипуляций
    browser.quit()