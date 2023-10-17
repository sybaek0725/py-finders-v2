from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# import os
# os.system("pause")

while True:
    # 검색어 입력 받기
    search_query = input("검색어를 입력하세요: ")

    if search_query:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument("--disable-extensions")

        # chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--start-maximized")

        driver2 = webdriver.Chrome(options=chrome_options)
        driver3 = webdriver.Chrome(options=chrome_options)
        driver4 = webdriver.Chrome(options=chrome_options)
        driver5 = webdriver.Chrome(options=chrome_options)
        driver6 = webdriver.Chrome(options=chrome_options)

        # 2. Findchips :
        driver2.get('https://www.findchips.com/')

        # 검색 자동화
        search_box2 = driver2.find_element(By.CLASS_NAME, 'search-field')
        search_box2.send_keys(search_query)
        search_box2.send_keys(Keys.RETURN)

        time.sleep(3)

        # 3. Find IC :
        driver3.get('https://www.findic.kr/')

        # 검색 자동화
        search_box3 = driver3.find_element(By.ID, 'search-kw')
        search_box3.send_keys(search_query)
        search_box3.send_keys(Keys.RETURN)

        time.sleep(3)

        # 4. Partsner :
        driver4.get('http://www.partsner.com/')

        # 검색 자동화
        search_box4 = driver4.find_element(By.ID, 'q_txt')
        search_box4.send_keys(search_query)
        search_box4.send_keys(Keys.RETURN)

        time.sleep(3)

        # 5. 올파츠 :
        driver5.get('https://www.allparts.co.kr/')

        ID = 'mworksk2'
        PW = 'tvp5150am1pbsr'

        # 로그인 자동화
        login_id_box5 = driver5.find_element(By.ID, 'user_id')
        login_id_box5.send_keys(ID)
        login_pw_box5 = driver5.find_element(By.ID, 'pswd')
        login_pw_box5.send_keys(PW)
        login_pw_box5.send_keys(Keys.RETURN)

        # 로그인 후 비밀변호 변경 팝업 닫기
        wait = WebDriverWait(driver5, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'btnHideWeek'))).click()


        # 검색 자동화
        search_box5 = driver5.find_element(By.ID, 'search_part')
        search_box5.send_keys(search_query)
        search_box5.send_keys(Keys.RETURN)

        time.sleep(3)

        # 6. Net Components :
        driver6.get('https://m.netcomponents.com/ko/home/index/')
        # driver6.get('https://m.netcomponents.com/ko/account/login')

        NUM = '123456'
        ID = 'mworksk'
        PW = 'Tvp5150am1'

        # 로그인 자동화 (!외부 이슈: 계정 번호 없음 ❌)
        # 로그인 후 페이지 이동 관련 테스트를 위해 회원가입 시도하였지만, 자격 요건이 있어, 중단함
        # 회원가입 경로 : https://m.netcomponents.com/ko/register/step1

        # login_num_box6 = driver6.find_element(By.ID, 'AccountNumber')
        # login_num_box6.send_keys(NUM)
        # login_id_box6 = driver6.find_element(By.ID, 'UserName')
        # login_id_box6.send_keys(ID)
        # login_pw_box6 = driver6.find_element(By.ID, 'Password')
        # login_pw_box6.send_keys(PW)
        # login_pw_box6.send_keys(Keys.RETURN)

        # 검색 자동화
        search_box6 = driver6.find_element(By.CLASS_NAME, 'searched-part')
        search_box6.send_keys(search_query)
        search_box6.send_keys(Keys.RETURN)

        # 7


    else:
        # print("검색어를 입력하지 않았습니다.")
        search_query = input("검색어를 입력하지 않았습니다. 검색어를 입력해주세요: ")

