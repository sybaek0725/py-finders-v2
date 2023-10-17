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
        driver7 = webdriver.Chrome(options=chrome_options)
        driver8 = webdriver.Chrome(options=chrome_options)
        driver9 = webdriver.Chrome(options=chrome_options)
        driver10 = webdriver.Chrome(options=chrome_options)
        driver11 = webdriver.Chrome(options=chrome_options)
        driver12 = webdriver.Chrome(options=chrome_options)
        driver13 = webdriver.Chrome(options=chrome_options)
        driver14 = webdriver.Chrome(options=chrome_options)
        driver15 = webdriver.Chrome(options=chrome_options)
        driver16 = webdriver.Chrome(options=chrome_options)
        driver17 = webdriver.Chrome(options=chrome_options)
        driver18 = webdriver.Chrome(options=chrome_options)
        driver19 = webdriver.Chrome(options=chrome_options)
        driver20 = webdriver.Chrome(options=chrome_options)
        driver21 = webdriver.Chrome(options=chrome_options)

        # 1. Findchips : 🟢 검색
        driver2.get('https://www.findchips.com/')

        # 검색 자동화
        search_box2 = driver2.find_element(By.CLASS_NAME, 'search-field')
        search_box2.send_keys(search_query)
        search_box2.send_keys(Keys.RETURN)
        time.sleep(3)


        # 2. Find IC : 🟢 검색
        driver3.get('https://www.findic.kr/')

        # 검색 자동화
        search_box3 = driver3.find_element(By.ID, 'search-kw')
        search_box3.send_keys(search_query)
        search_box3.send_keys(Keys.RETURN)
        time.sleep(3)


        # 3. Partsner : 🟢 검색
        driver4.get('http://www.partsner.com/')

        # 검색 자동화
        search_box4 = driver4.find_element(By.ID, 'q_txt')
        search_box4.send_keys(search_query)
        search_box4.send_keys(Keys.RETURN)
        time.sleep(3)


        # 4. Allparts (MICHAEL) : 🟢 검색, 🟢 로그인
        driver5.get('https://www.allparts.co.kr/')

        # 로그인 자동화
        ID = 'mworksk2'
        PW = 'tvp5150am1pbsr'

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


        # 5. Net Components : 🟢 검색, ❌ 로그인
        # 로그인 자동화 (!외부 이슈: 계정 번호 없음)
        # driver6.get('https://m.netcomponents.com/ko/account/login')

        # 로그인 후 페이지 이동 관련 테스트를 위해 회원가입 시도하였지만, 자격 요건이 있어, 중단함
        # 회원가입 경로 : https://m.netcomponents.com/ko/register/step1

        NUM = '123456'
        ID = 'mworksk'
        PW = 'Tvp5150am1'

        # login_num_box6 = driver6.find_element(By.ID, 'AccountNumber')
        # login_num_box6.send_keys(NUM)
        # login_id_box6 = driver6.find_element(By.ID, 'UserName')
        # login_id_box6.send_keys(ID)
        # login_pw_box6 = driver6.find_element(By.ID, 'Password')
        # login_pw_box6.send_keys(PW)
        # login_pw_box6.send_keys(Keys.RETURN)

        driver6.get('https://m.netcomponents.com/ko/home/index/')

        # 검색 자동화
        search_box6 = driver6.find_element(By.CLASS_NAME, 'searched-part')
        search_box6.send_keys(search_query)
        search_box6.send_keys(Keys.RETURN)
        time.sleep(3)


        # 6. IC Source : 🟢 검색, ❌ 로그인
        # driver7.set_window_size(1124, 850)
        driver7.get('https://icsource.com/Home/Index.aspx')

        # 로그인 자동화 (!내부 이슈: Password 요소 선택은 되지만, send_keys 에러 발생)

        ID = 'mworks'
        PW = 'Tvp5150am1!!'

        # login_id_box7 = driver7.find_element(By.XPATH, '/html/body/form/div[6]/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/input')
        # login_id_box7.send_keys(ID)
        # time.sleep(2)
        # login_pw_box7 = driver7.find_element(By.CLASS_NAME, 'passwordhidden')
        # login_pw_box7.click()
        # print('🩷🩷🩷🩷🩷 password', login_pw_box7)
        # print('🩷🩷🩷🩷🩷 password2', PW)
        # login_pw_box7.send_keys(PW)
        # print('🩷🩷🩷🩷🩷 login_pw_box7.send_keys(Keys.RETURN)', login_pw_box7.send_keys(Keys.RETURN))
        # login_pw_box7.send_keys(Keys.RETURN)

        # 검색 자동화
        search_box7 = driver7.find_element(By.ID, 'ctl00_txtSearchTerm')
        search_box7.send_keys(search_query)
        search_box7.send_keys(Keys.RETURN)


        # 7. Broker Forum : 🟢 검색, ❌ 로그인
        driver8.get('https://www.brokerforum.com/')

        # 로그인 자동화 (!외부 이슈: 로그인 계정 정보 신원을 확인할 수 없습니다~~ 문구 노출)
        ID = 'mworkskap'
        PW = 'Tvp5150am1!!'

        # login_id_box8 = driver8.find_element(By.ID, 'mainMenuLoginButton')
        # login_id_box8.click()
        # time.sleep(3)
        # login_id_box8 = driver8.find_element(By.ID, 'Session_Username')
        # login_id_box8.send_keys(ID)
        # time.sleep(3)
        # login_id_box8 = driver8.find_element(By.ID, 'Session_Password')
        # login_id_box8.send_keys(PW)
        # time.sleep(3)
        # login_id_box8.send_keys(Keys.RETURN)

        # 검색 자동화
        search_box8 = driver8.find_element(By.ID, 'originalFullPartNumber')
        search_box8.send_keys(search_query)
        search_box8.send_keys(Keys.RETURN)


        # 8. Digi Parts : 🟢 검색
        driver9.get('https://www.digipart.com/')

        # 검색 자동화
        search_box9 = driver9.find_element(By.ID, 'term')
        search_box9.send_keys(search_query)
        search_box9.send_keys(Keys.RETURN)


        # 9. HK Inventory : 🟢 검색
        driver10.get('https://www.hkinventory.com/')

        search_box10 = driver10.find_element('id', 'pnums')
        search_box10.send_keys(search_query)
        search_box10.send_keys(Keys.RETURN)


        # 10. Microchip Direct : 🟢 검색, ❌ 로그인
        driver11.get('https://www.microchipdirect.com/')

        # 로그인 자동화 (!내부 이슈: 로그인 버튼 선택 시, popover가 노출되는데, 요소 선택 시 popover가 닫혀서 확인 불가 (방법 확인 필요...))
        ID = 'bmselec@bmselec.co.kr'
        PW = 'Tvp5150am1!'

        # input_btn_box11 = driver11.find_element(By.ID, 'loginButton')
        # input_btn_box11.click()
        # time.sleep(3)

        # 검색 자동화
        search_box11 = driver11.find_element(By.XPATH, '/html/body/div[8]/div/div[1]/div[2]/div/div/div/div[1]/nav[1]/ul[2]/div/div/div[1]/div/input')
        search_box11.send_keys(search_query)
        search_box11.send_keys(Keys.RETURN)


        # 11. TI STORE : 🟢 검색, 🟢 로그인
        # 로그인 자동화
        driver12.get('https://login.ti.com/as/authorization.oauth2?response_type=code&scope=openid%20email%20profile&client_id=DCIT_ALL_WWW-PROD&state=ASyLnI6G2yrRzK62u53IkdH9_T0&redirect_uri=https%3A%2F%2Fwww.ti.com%2Foidc%2Fredirect_uri%2F&nonce=EB0zAM0EHXE83JqVK1Bagm3Wa84cROtpvDQ23RP6LrY&response_mode=form_post')

        ID = 'INFO@OLIVE-EMS.COM'
        PW = 'Tvp5150am1!!'

        login_id_box12 = driver12.find_element(By.ID, 'username')
        login_id_box12.send_keys(ID)
        time.sleep(2)
        driver12.find_element(By.ID, 'nextbutton').click()

        login_pw_box12 = driver12.find_element(By.XPATH, '/html/body/main/div/div/div/form/div/div[2]/ti-password/input')
        login_pw_box12.send_keys(PW)
        login_pw_box12.send_keys(Keys.RETURN)

        time.sleep(2)

        # 검색 자동화
        search_box12 = driver12.find_element(By.CSS_SELECTOR, 'div#searchboxheader input')
        search_box12.send_keys(search_query)
        search_box12.send_keys(Keys.RETURN)


        # 12. AD Web : ❌ 검색, ❌ 로그인
        driver13.get('https://www.analog.com/en/index.html')

        # 로그인 자동화 (!내부 이슈 : 아날로그 디바이스 쿠키 정책 하단 팝업이 노출, 해결 방법 확인 필요)
        # 로그인 X 아날 로그 디 바이스 쿠키 정책 하단 팝업이 노출됨
        # driver13.get('https://analogb2c.b2clogin.com/analogb2c.onmicrosoft.com/b2c_1a_adi_signuporsigninsocial/oauth2/v2.0/authorize?client_id=5a2d9b38-78a8-415d-8565-5229c9ed6ed2&scope=https%3A%2F%2Fanalogb2c.onmicrosoft.com%2Fmyanalog%2Fwrite%20openid%20profile%20offline_access&redirect_uri=https%3A%2F%2Fwww.analog.com%2Fredirect-sso.html&client-request-id=a16432a9-f262-4503-9776-eacc24872a02&response_mode=fragment&response_type=code&x-client-SKU=msal.js.browser&x-client-VER=2.28.0&client_info=1&code_challenge=n807L_U0p5vFO0JItJCSWPlnIoWpDE3WogkpxY3XSY4&code_challenge_method=S256&nonce=181a94b4-d9ca-4232-9625-0bb4488bac18&state=eyJpZCI6IjAyMWU0OTRjLTg4ZDQtNGUyYi05OTc2LTA0NTZmMWM5MGE2NyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D%7Chttps%3A%2F%2Fmy.analog.com%2Fen%2Fapp&ui_locales=en&startUrl=https://my.analog.com/en/app&cookieAccepted=null')
        # driver.maximize_window()
        # driver13.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        # time.sleep(3)

        ID = 'bmselec@bmselec.co.kr'
        PW = 'Tvp5150am1!!'

        # login_id_box13 = driver13.find_element(By.ID, 'signInName')
        # login_id_box13.send_keys(ID)
        # time.sleep(3)
        #
        # login_pw_box13 = driver13.find_element(By.ID, 'password')
        # login_pw_box13.send_keys(PW)
        # time.sleep(3)

        # 검색 자동화 (!내부 이슈 : 아날로그 디바이스 쿠키 정책 하단 팝업이 노출, 해결 방법 확인 필요)
        search_box13 = driver13.find_element('id', 'text-global-search')
        search_box13.send_keys(search_query)
        search_box13.send_keys(Keys.RETURN)


        # 13. Digikey (Olive) : ❌ 검색, ❌ 로그인
        driver14.get('https://www.digikey.kr/')

        # 로그인 자동화 (!내부 이슈 : 404 로봇이 아님을 증명해야하는 화면 노출)
        # driver14.get('https://auth.digikey.com/as/authorization.oauth2?response_type=code&client_id=pa_wam&redirect_uri=https%3A%2F%2Fwww.digikey.kr%2Fpa%2Foidc%2Fcb&state=eyJ6aXAiOiJERUYiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiMnMiLCJzdWZmaXgiOiJmOEx2dEQuMTY5NTM2OTQyMSJ9..d3nF437ZPvg3QdKkDo_K1A.FA3TFUieEfwgAkWAPtVRuFjG7txjlzoieI19X_EpMRw8PnCG0hxhwJJVMlZoZhi1W7uK2bwWEjNWJYpXjFSbwhNDSqbNAFacEKwCCTMQV6lPwG7WIbYQfbOzk017vsOg66YVqocP9a4yj1dYYutPdulzvYBfFe4zJ9Tmpvq7efw.UFToSImrG3hF8eZNousKUw&nonce=kNKpYHE7UPwlT-maF5aS5ltAusqHv5V4IF9z0DX-M64&scope=openid%20address%20email%20phone%20profile&vnd_pi_requested_resource=https%3A%2F%2Fwww.digikey.kr%2FMyDigiKey%2FLogin%3Fsite%3DKR%26lang%3Den%26returnurl%3Dhttps%253A%252F%252Fwww.digikey.kr%252Fen&vnd_pi_application_name=DigikeyProd-Mydigikey')

        ID = 'info@olive-ems.com'
        PW = 'Tvp5150am1!!'

        # login_id_box14 = driver14.find_element(By.XPATH, '/html/body/div/div[3]/div/form/div[2]/input')
        # login_id_box14.send_keys(ID)
        # time.sleep(2)
        # login_pw_box14 = driver14.find_element(By.XPATH, '/html/body/div/div[3]/div/form/div[3]/input')
        # login_pw_box14.send_keys(PW)
        # time.sleep(2)
        # login_pw_box14.send_keys(Keys.RETURN)

        # 검색 자동화 (!내부 이슈 : 404 로봇이 아님을 증명해야하는 화면 노출(간혈적..?))
        # search_box14 = driver14.find_element(By.CLASS_NAME, 'header__searchinput')
        # search_box14.send_keys(search_query)
        # time.sleep(3)
        # search_box14.send_keys(Keys.RETURN)
        # driver.find_element('id', 'header-search-button').click()


        # 14. Mouser : ❌ 검색, ❌ 로그인
        driver15.get('https://www.mouser.kr/')

        # 로그인 자동화 (!내부 이슈 : "당신이 인간인지 확인해주세요" 문구 노출, 해결 방법 확인 필요)

        # Mouser 홈에서 로그인 화면 진입 시나리오
        # time.sleep(3)
        # driver15.find_element(By.ID, 'mblAccnt').click()
        # time.sleep(3)
        # driver15.find_element(By.ID, 'lnkLoginMobile').click()
        # time.sleep(3)

        # Mouser 로그인 화면 진입 시나리오
        # driver15.get('https://www.mouser.kr/MyAccount/MouserLogin?qs=0gZ0gv0KDwsgKSbV9hbU5Q%3d%3d')

        ID = 'Amypark'
        PW = 'tvp5150am1'

        # login_id_box15 = driver15.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/div[1]/div[4]/form/div[1]/input')
        # login_id_box15.send_keys(ID)
        # login_pw_box15 = driver15.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/div[1]/div[4]/form/div[2]/input')
        # login_pw_box15.send_keys(PW)
        # time.sleep(2)
        # login_pw_box15.send_keys(Keys.RETURN)
        # time.sleep(2)

        # 검색 자동화 (!내부 이슈 : 로그인 후, "당신이 인간인지 확인해주세요" 문구 노출, 해결 방법 확인 필요)
        # search_box15 = driver15.find_element(By.CLASS_NAME, 'search-input')
        # time.sleep(3)
        # search_box15.send_keys(search_query)
        # time.sleep(3)
        # search_box15.send_keys(Keys.RETURN)


        # 15. Arrow : 🟢 검색, 🟢 로그인
        # 로그인 자동화
        driver16.get('https://www.arrow.com/ko-kr/login?gotoSplash=true&url=')

        ID = 'mjang@microworks.co.kr'
        PW = 'Tvp5150am1pbsr!'

        login_id_box16 = driver16.find_element(By.XPATH, '/html/body/div[1]/div[12]/div[3]/div/div/div/form/div[3]/input')
        login_id_box16.send_keys(ID)
        time.sleep(2)
        login_pw_box16 = driver16.find_element(By.XPATH, '/html/body/div[1]/div[12]/div[3]/div/div/div/form/div[4]/input')
        login_pw_box16.send_keys(PW)
        time.sleep(2)
        login_pw_box16.send_keys(Keys.RETURN)
        # 로그인되는 속도가 느려서 타임 걸어놓음
        time.sleep(10)

        # 검색 자동화
        search_box16 = driver16.find_element(By.CLASS_NAME, 'Search-bar-select-input')
        search_box16.send_keys(search_query)
        time.sleep(3)
        search_box16.send_keys(Keys.RETURN)


        # 16. Element14 : 🟢 검색, 🟢 로그인
        # 로그인 자동화
        driver17.get('https://kr.element14.com/webapp/wcs/stores/servlet/LogonForm?myAcctMain=1&catalogId=15001&storeId=10187&langId=-9&URL=https%3A%2F%2Fkr.element14.com%2F')
        time.sleep(3)

        ID = 'Steelan'
        PW = 'tvp5150am1'
        
        login_id_box17 = driver17.find_element(By.XPATH, '/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[4]/input')
        login_id_box17.send_keys(ID)
        time.sleep(3)
        login_pw_box17 = driver17.find_element(By.XPATH, '/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[7]/input')
        login_pw_box17.send_keys(PW)
        time.sleep(3)
        login_pw_box17.send_keys(Keys.RETURN)
        # 로그인되는 속도가 느려서 타임 걸어놓음 (7~8초로 해도 될듯)
        time.sleep(10)

        # 검색 자동화
        search_box17 = driver17.find_element(By.ID, 'SimpleSearchForm_SearchTerm')
        search_box17.send_keys(search_query)
        time.sleep(3)
        search_box17.send_keys(Keys.RETURN)
    
        
        # 17. Verical : 🟢 검색, 🟢 로그인
        # 로그인 자동화
        driver18.get('https://www.verical.com/sign-in?return=%2F')

        ID = 'mjang@microworks.co.kr'
        PW = 'Tvp5150am1pbsr!'

        login_id_box18 = driver18.find_element(By.XPATH, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[1]/div/div[1]/div/input')
        login_id_box18.send_keys(ID)
        time.sleep(3)
        login_pw_box18 = driver18.find_element(By.XPATH, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[2]/div/div[1]/div/input')
        login_pw_box18.send_keys(PW)
        time.sleep(3)
        login_pw_box18.send_keys(Keys.RETURN)
        # 로그인되는 속도가 느려서 타임 걸어놓음 (7~8초로 해도 될듯)
        time.sleep(8)

        # 검색 자동화
        search_box18 = driver18.find_element(By.ID, 'mat-input-1')
        search_box18.send_keys(search_query)
        time.sleep(3)
        search_box18.send_keys(Keys.RETURN)


        driver19.get('https://www.chip1stop.com/KOR/ko/login')
        time.sleep(3)
        
        # 로그인 자동화
        ID = 'mworksk'
        PW = 'mworksk123'

        login_id_box19 = driver19.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/form/dl/dd[1]/input')
        login_id_box19.send_keys(ID)
        time.sleep(3)
        login_pw_box19 = driver19.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/form/dl/div/dd/input')
        login_pw_box19.send_keys(PW)
        time.sleep(3)
        login_pw_box19.send_keys(Keys.RETURN)
        time.sleep(5)

        # 검색 자동화
        search_box19 = driver19.find_element('id', 'headerKeywordSearch')
        search_box19.send_keys(search_query)
        time.sleep(3)
        search_box19.send_keys(Keys.RETURN)


        # 19. LCSC : 🟢 검색
        driver20.get('https://www.lcsc.com/')
        time.sleep(3)

        # 검색 자동화
        driver20.find_element(By.CSS_SELECTOR, "div.v-card__title button").click()
        time.sleep(3)
        search_box20 = driver20.find_element('id', 'input-23')
        search_box20.send_keys(search_query)
        search_box20.send_keys(Keys.RETURN)


        # 20. Trusted Parts : ❌ 검색
        driver21.get('https://www.trustedparts.com/en')
        # 검색 자동화
        # 🚨 X 당신이 로봇이 아님을 확인하기 위한 필수 절차입니다. 화면 노출
        time.sleep(3)
        search_box21 = driver21.find_element(By.ID, 'searchText')
        search_box21.send_keys(search_query)
        time.sleep(3)
        search_box21.send_keys(Keys.RETURN)

    else:
        # print("검색어를 입력하지 않았습니다.")
        search_query = input("검색어를 입력하지 않았습니다. 검색어를 입력해주세요: ")

