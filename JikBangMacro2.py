# CopyRight S.J.Yoon @HAFS @HAFSLAB2020
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.webdriver.support.ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

driver = webdriver.Chrome('C:/Users/SJYoon/chromedriver.exe',desired_capabilities=capa)  # webdriver 객체 생성

driver.implicitly_wait(0.3)  # 웹 자원 로딩을 위한 대기
#driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#driver.execute_script("window.stop();")


url: str = 'http://www.hafsjickbang.com/'
id: str = "qwerty"
pw: str = "asdfghjkl"

rf1 = 6
rf2 = 6

driver.get(url)  # url 로드

driver.find_element_by_name('id').send_keys(id)  # 로그인 정보 입력
driver.find_element_by_name('password').send_keys(pw)

driver.find_element_by_xpath('/html/body/div[1]/div/form/div[3]/button').click()  # 로그인

# 회화실 예약
while True:
    try:
        driver.find_element_by_xpath('/html/body/div/div/div/div[' + str(rf1) + ']/div[4]/form/button').click()

    except Exception as ex:
        print("Error", ex)
        break

while True:
    try:
        driver.find_element_by_xpath('/html/body/div/div/div/div[' + str(rf2) + ']/div[5]/form/button').click()

    except Exception as ex:
        print("Error", ex)
        break
