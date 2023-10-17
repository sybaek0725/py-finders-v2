from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 사이트 리스트
sites = [
    # 1. Findchips : 🟢 검색
    # {
    #     'url': 'https://www.findchips.com/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[2]/div/div/div[1]/div/form/span/input',
    #     },
    #     'login': None
    # },
    # 2. Find IC : 🟢 검색
    # {
    #     'url': 'https://www.findic.kr/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[4]/div[2]/form/input[1]',
    #     },
    #     'login': None
    # },
    # 3. Partsner : 🟢 검색
    # {
    #     'url': 'http://www.partsner.com/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[2]/div[1]/div/ul/li[2]/input',
    #     },
    #     'login': None
    # },
    # 4. Allparts (MICHAEL) : 🟢 검색, 🟢 로그인
    {
        'url': 'https://www.allparts.co.kr/',
        'entry': False,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[1]/div[3]/div/input',
        },
        'login': {  
            'entry': True,
            'selector': [By.ID, By.ID],
            'element': ['user_id', 'pswd'],
        },
        'user_info': {
            'user_id': 'mworksk2',
            'user_pw': 'tvp5150am1pbsr'
        },
    },
    # 5. Net Components : 🟢 검색, ❌ 로그인
    # {
    #     'url': 'https://m.netcomponents.com/ko/home/index/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.CLASS_NAME,
    #         'element': 'searched-part',
    #     },
    #     'login': {  
    #         'entry': False,
    #         'selector': [By.ID, By.ID, By.ID], # 계정 번호가 있어 분기 필요
    #         'element': ['123456', 'UserName', 'Password'],
    #     },
    #     'user_info': {
    #         'user_id': 'mworksk',
    #         'user_pw': 'Tvp5150am1'
    #     },
    # },
    # 6. IC Source : 🟢 검색, ❌ 로그인
    # {
    #     'url': 'https://icsource.com/Home/Index.aspx',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/form/div[6]/div[4]/div[2]/div/div[1]/div[2]/div/input[2]',
    #     },
    #     'login': {  
    #         'entry': False,
    #         'selector': [By.XPATH, By.CLASS_NAME], 
    #         'element': ['/html/body/form/div[6]/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/input', 'passwordhidden'],
    #     },
    #     'user_info': {
    #         'user_id': 'mworks',
    #         'user_pw': 'Tvp5150am1!!'
    #     },
    # },
    # 7. Broker Forum : 🟢 검색, ❌ 로그인
    # 로그인 전 아래 로직 추가되야 함
    # login_id_box8 = driver8.find_element(By.ID, 'mainMenuLoginButton')
    # login_id_box8.click()
    # {
    #     'url': 'https://www.brokerforum.com/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div[1]/input',
    #     },
    #     'login': {  
    #         'entry': False,
    #         'selector': [By.ID, By.ID], 
    #         'element': ['Session_Username', 'Session_Password'],
    #     },
    #     'user_info': {
    #         'user_id': 'mworks',
    #         'user_pw': 'Tvp5150am1!!'
    #     },
    # },
    # 8. Digi Parts : 🟢 검색
    # {
    #     'url': 'https://www.digipart.com/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[1]/div/div[1]/form/div/div/input',
    #     },
    #     'login': None
    # },
    # 9. HK Inventory : 🟢 검색
    # {
    #     'url': 'https://www.hkinventory.com/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/center/div[1]/div[1]/form/div[1]/input[1]',
    #     },
    #     'login': None
    # },

    # 10. Microchip Direct : 🟢 검색, ❌ 로그인
    # 로그인 전 아래 로직 추가되야 함
    # input_btn_box11 = driver11.find_element(By.ID, 'loginButton')
    # input_btn_box11.click()
    # {
    #     'url': 'https://www.microchipdirect.com/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[8]/div/div[1]/div[2]/div/div/div/div[1]/nav[1]/ul[2]/div/div/div[1]/div/input',
    #     },
    #     'login': {  
    #         'entry': False,
    #         'selector': [By.ID, By.ID], 
    #         'element': ['Session_Username', 'Session_Password'],
    #     },
    #     'user_info': {
    #         'user_id': 'bmselec@bmselec.co.kr',
    #         'user_pw': 'Tvp5150am1!'
    #     },
    # },
    # 11. TI STORE : 🟢 검색, 🟢 로그인
    # 로그인 아이디 입력 후 아래 로직 추가되어야 함
    # driver12.find_element(By.ID, 'nextbutton').click()
    # {
    #     'url': 'https://www.ti.com/ko-kr/homepage.html',
    #     'entry': False,
    #     'search': {
    #         'selector': By.CSS_SELECTOR,
    #         'element': 'div#searchboxheader input',
    #     },
    #     'login': {  
    #         'entry': False,
    #         'selector': [By.ID, By.XPATH], 
    #         'element': ['username', '/html/body/main/div/div/div/form/div/div[2]/ti-password/input'],
    #     },
    #     'user_info': {
    #         'user_id': 'INFO@OLIVE-EMS.COM',
    #         'user_pw': 'Tvp5150am1!!'
    #     },
    # },
    ##### 수정전
    # 12. AD Web : ❌ 검색, ❌ 로그인
    # {
    #     'url': 'https://www.analog.com/en/index.html',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/header/section/div/div[2]/form/input',
    #     },
    #     'login': {'signInName': 'bmselec@bmselec.co.kr', 'password': 'Tvp5150am1!!'}
    # },
    # 13. Digikey (Olive) : ❌ 검색, ❌ 로그인
    # {
    #     'url': 'https://www.digikey.kr/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/header/div[1]/div[2]/div/div[2]/div[2]/input',
    #     },
    #     'login': {'pa_wam': 'pa_wam', 'pa_returnurl': 'https://www.digikey.kr/pa/oidc/cb', 'vnd_pi_requested_resource': 'https://www.digikey.kr/MyDigiKey/Login?site=KR&lang=en&returnurl=https%3A%2F%2Fwww.digikey.kr%2Fen', 'vnd_pi_application_name': 'DigikeyProd-Mydigikey', 'openid': 'openid address email phone profile', 'state': 'eyJ6aXAiOiJERUYiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiMnMiLCJzdWZmaXgiOiJmOEx2dTQuMTY5NTM2OTQyMSJ9..9g6cA9FwaZMRCDUhEJibjg.cMQNTSxEjgIiAxF0fgfcu7EEh3brswfHH4eMxXTzTShgtLbNAGJDruuWCRjjLRFUtso1O8tNSvMOKFbjew5CzoLTTK5w2kRRbDAdxQv_6dW5F6tjrRkNc4VhAZbmo5DcNtrNv4J50uPugVQbDyJ-wvDv6mgDCdWZcDtjB5JQ5flnBOCxM_C3K67_fegcZZWRZQtZ7hE5soD2tbnogGiNrC2RF4O2QYWwqk8y19ksYZyyU5J4gCQb7shI-58SgWCOw3W2ID7D7mDK-L7yfn9Dzmo6K_PkvC6n0qxrTgYH9toQCVngEOYVDG-1k6Mg3_VXEd6b9kJR9gO3jtGzYZbHhrRdFQ0hjJ9UJjPw8pH3lPs7YthKuJZlcpQfRbmwOdmVKW7hF6l1f5sh8QHVm8iCfGWSTBFWPvczZY7CNw0VUvGXW4hdDr-BQ5gj7FlmBfJhHNgB4sv-kKwEQ5JbKnhXZSLNVzrxMvNRCSbMRSuP6yH7m1YfFwDSrRSTSEFzdGh6uITdG6ZuIbi8OQKT87v8S_m1aM6Ct17kiJNlLKD5APz6oTk1WbSDFKqS5o8g9kAJSitnFJktfTQDgoxCssA49ofM_f0VqDhT3nnS3fQ3obm1RzgNYmzIHz8uIenB7TwWxOnBoJ-gQlFUvINWJ9WTigB4M5nNvLhB6i-WjxTR5kYGXzjG7QdCxD0bOzX-Dmc2_m0A5pMPSiR5Wl5p8ciitGFN6aWftDz7XvDg6VQ-TfDxJ8FwxmDPv-TC1v4T0XDpziEJyGxS6B6GDpXe1eN1VzgA5PCE0kE5_w9i6S1jOStW5TRGkFvGEHVz1qHjFw4t0RkU6k5F8CjPgo0RDpF1-hHEw7wiXjm8A5z6UchB5RvR1gmD3iO6Pd6jkYhOmKZCXpDVhvz4Wig60S5jJt6TS5DXD6B8pSVMbjk0YR5YDB9cVwGRw0CkGD3NCt7cDkE2M6zTrzWf8gBcKHuJE5j7LXCyz6J2GJzUC4tT7Kg3Qc8YXNi5VD2L0CRjX8GpWdh6XC3XJj2jC0uB7EgkjB8WgXg5gXkwCxSkUgU5bglJW3cGXDXjb9mFb7D8J8zgW6vQJ4CgER4EWCiR8G3m0RBbA6Yghk2VDmBDs0g6LwgBkCE8jiYpJvIg9C6goz5NJF5B9oRQ9WDgNDSCDXGbzJ1jO5ECjiR6Bd9LJ2YC0yfJNiFg6iNCz0z8j5kzkkL1Q8JbW9jh5RwW5Pf9IwjB6Mf7jEw2h0Wqvgg-gHGo8'}
    # },
    # 14. Mouser : ❌ 검색, ❌ 로그인
    # {
    #     'url': 'https://www.mouser.kr/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/header/div[4]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/input[1]',
    #     },
    #     'login': None
    # },
    # 15. Arrow : 🟢 검색, 🟢 로그인
    {
        'url': 'https://www.arrow.com/ko-kr/login?gotoSplash=true&url=',
        'entry': False,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[1]/header/div/div[1]/div[1]/div/div[1]/form/div/input[1]',
        },
        'login': {  
            'entry': False,
            'selector': [By.XPATH, By.XPATH], 
            'element': ['/html/body/div[1]/div[12]/div[3]/div/div/div/form/div[3]/input', '/html/body/div[1]/div[12]/div[3]/div/div/div/form/div[4]/input'],
        },
        'user_info': {
            'user_id': 'mjang@microworks.co.kr',
            'user_pw': 'Tvp5150am1pbsr!'
        },
    },
    # 16. Element14 : 🟢 검색, 🟢 로그인
    {
        'url': 'https://kr.element14.com/webapp/wcs/stores/servlet/LogonForm?myAcctMain=1&catalogId=15001&storeId=10187&langId=-9&URL=https%3A%2F%2Fkr.element14.com%2F',
        'entry': False,
        'search': {
            'selector': By.ID,
            'element': 'SimpleSearchForm_SearchTerm',
        },
        'login': {  
            'entry': False,
            'selector': [By.XPATH, By.XPATH], 
            'element': ['/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[4]/input', '/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[7]/input'],
        },
        'user_info': {
            'user_id': 'Steelan',
            'user_pw': 'tvp5150am1'
        },
    },
    # 17. Verical : 🟢 검색, 🟢 로그인
    {
        'url': 'https://www.verical.com/sign-in?return=%2F',
        'entry': False,
        'search': {
            'selector': By.ID,
            'element': 'mat-input-1',
        },
        'login': {  
            'entry': False,
            'selector': [By.XPATH, By.XPATH], 
            'element': ['/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[1]/div/div[1]/div/input', '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[2]/div/div[1]/div/input'],
        },
        'user_info': {
            'user_id': 'mjang@microworks.co.kr',
            'user_pw': 'Tvp5150am1pbsr!'
        },
    },
    # 18. Chip One Stop : 🟢 검색, 🟢 로그인
    {
        'url': 'https://www.chip1stop.com/KOR/ko/login',
        'entry': False,
        'search': {
            'selector': By.ID,
            'element': 'headerKeywordSearch',
        },
        'login': {  
            'entry': False,
            'selector': [By.XPATH, By.XPATH], 
            'element': ['/html/body/div[1]/main/div/div[1]/form/dl/dd[1]/input', '/html/body/div[1]/main/div/div[1]/form/dl/div/dd/input'],
        },
        'user_info': {
            'user_id': 'mworksk',
            'user_pw': 'mworksk123'
        },
    },
    # 19. LCSC : 🟢 검색
    # {
    #     'url': 'https://www.lcsc.com/',
    #     'entry': True,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/input',
    #     },
    #     'login': None
    # },
    # 20. Trusted Parts : ❌ 검색
    # {
    #     'url': 'https://www.trustedparts.com/en',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[1]/nav/div/div[1]/div/div/div/div/input',
    #     },
    #     'login': None
    # }
]

drivers = []
num_drivers = len(sites)
print('🩵🩵🩵🩵🩵🩵🩵', len(sites))

def search_and_login(driver, search_query, index):
    driver.get(sites[index]['url'])

    if sites[index]['entry']:
        driver.find_element(By.CSS_SELECTOR, "div.v-card__title button").click()

    # 로그인 자동화 
    if sites[index]['login']:
        login_box = driver.find_element(sites[index]['login']['selector'][0], sites[index]['login']['element'][0])
        login_box.send_keys(sites[index]['user_info']['user_id'])
        time.sleep(3)
        login_box = driver.find_element(sites[index]['login']['selector'][1], sites[index]['login']['element'][1])
        login_box.send_keys(sites[index]['user_info']['user_pw'])
        time.sleep(3)
        login_box.send_keys(Keys.RETURN)
        time.sleep(8)

        if sites[index]['login']['entry']:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.ID, 'btnHideWeek'))).click()

    # 검색 자동화     
    search_box = driver.find_element(sites[index]['search']['selector'], sites[index]['search']['element'])
    search_box.send_keys(search_query)
    time.sleep(3)
    search_box.send_keys(Keys.RETURN)

    # 새 탭으로 열기
    if index != num_drivers - 1:
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[index + 1])

while True:
    search_query = input("검색어를 입력하세요: ")

    if search_query:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        drivers.append(driver)

        for index in range(num_drivers):
            search_and_login(drivers[0], search_query, index)

    else:
        print("검색어를 입력하지 않았습니다. 검색어를 입력해주세요.")
