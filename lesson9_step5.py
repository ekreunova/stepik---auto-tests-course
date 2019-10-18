from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x1):
  return str(math.log(abs(12*math.sin(int(x1)))))



try :
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 12 секунд, пока в поле не будет 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100"))

    
    button = browser.find_element_by_id("book")
    button.click()


    

    x = browser.find_element_by_id("input_value")
    x1 = x.text
    
    y = calc(x1)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)


    # Отправляем заполненную форму
    button2 = browser.find_element_by_id("solve")
    button2.click()

    
    

finally :
   # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

