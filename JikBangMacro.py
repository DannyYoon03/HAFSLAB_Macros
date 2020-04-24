# CopyRight S.J.Yoon @HAFS @HAFSLAB2020
from selenium import webdriver


driver = webdriver.Chrome('C:/Users/SJYoon/chromedriver.exe')  # webdriver 객체 생성

driver.implicitly_wait(3)  # 웹 자원 로딩을 위한 대기



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
