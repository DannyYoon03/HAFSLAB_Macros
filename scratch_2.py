from selenium import webdriver

driver = webdriver.Chrome('C:/Users/SJYoon/chromedriver.exe') # webdriver 객체 생성

driver.implicitly_wait(3) # 웹 자원 로딩을 위한 대기시간

url = 'http://www.hafsjickbang.com/'
id = 'qwerty'
pw = 'asdfghjkl'

driver.get(url) # url 로드

driver.find_element_by_name('id').send_keys(id) #로그인 정보 입력
driver.find_element_by_name('password').send_keys(pw)

driver.find_element_by_xpath('/html/body/div[1]/div/form/div[3]/button').click() #로그인



