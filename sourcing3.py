from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 사이트 리스트
sites = [
    # 5. Net Components : 🟢 검색, ❌ 로그인 (!외부 이슈: 계정 번호 없음)
    # {
    #     'name': 'net-components', 
    #     'url': 'https://m.netcomponents.com/ko/home/index/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.CLASS_NAME,
    #         'element': 'searched-part',
    #     },
    #     'login': {  
    #         'selector': [By.ID, By.ID, By.ID], # 계정 번호가 있어 분기 필요
    #         'element': ['123456', 'UserName', 'Password'],
    #     },
    #     'user_info': {
    #         'user_num': '',
    #         'user_id': 'mworksk',
    #         'user_pw': 'Tvp5150am1'
    #     },
    # },
    # 6. IC Source : 🟢 검색, ❌ 로그인 (!내부 이슈: Password 요소 선택은 되지만, send_keys 에러 발생)
    {
        'name': 'ic-source',
        'url': 'https://icsource.com/Home/Index.aspx',
        'entry': False,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/form/div[6]/div[4]/div[2]/div/div[1]/div[2]/div/input[2]',
        },
        'login': {  
            'selector': [By.XPATH, By.CLASS_NAME], 
            'element': ['/html/body/form/div[6]/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/input', 'passwordhidden'],
        },
        'user_info': {
            'user_id': 'mworks',
            'user_pw': 'Tvp5150am1!!'
        },
    },
    # 7. Broker Forum : 🟢 검색, ❌ 로그인 (!외부 이슈: 로그인 계정 정보 신원을 확인할 수 없습니다~~ 문구 노출)
    # {
    #     'name': 'broker-forum',
    #     'url': 'https://www.brokerforum.com/',
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div[1]/input',
    #     },
    #     'login': {  
    #         'selector': [By.ID, By.ID], 
    #         'element': ['Session_Username', 'Session_Password'],
    #     },
    #     'user_info': {
    #         'user_id': 'mworks',
    #         'user_pw': 'Tvp5150am1!!'
    #     },
    # },
    # 10. Microchip Direct : 🟢 검색, ❌ 로그인 (!내부 이슈: 로그인 버튼 선택 시, popover가 노출되는데, 요소 선택 시 popover가 닫혀서 확인 불가 (방법 확인 필요...))
    {
        'name': 'microchip-direct',
        'url': 'https://www.microchipdirect.com/',
        'entry': False,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[8]/div/div[1]/div[2]/div/div/div/div[1]/nav[1]/ul[2]/div/div/div[1]/div/input',
        },
        'login': {  
            'selector': [By.ID, By.ID], 
            'element': ['loginEmail', 'loginPassword'],
        },
        'user_info': {
            'user_id': 'bmselec@bmselec.co.kr',
            'user_pw': 'Tvp5150am1!'
        },
    },
    # 12. AD Web : ❌ 검색, ❌ 로그인 (!내부 이슈 : 아날로그 디바이스 쿠키 정책 하단 팝업이 노출, 해결 방법 확인 필요(검색은 팝업 노출된 상태에서 검색 결과 화면 이동 처리됨))
    {
        'name': 'ad-web', 
        'url': 'https://www.analog.com/en/index.html',
        'entry': False,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/header/section/div/div[2]/form/input',
        },
        'login': {},
        'user_info': {
            'user_id': 'bmselec@bmselec.co.kr',
            'user_pw': 'Tvp5150am1!!'
        } 
    },
    # 13. Digikey (Olive) : ❌ 검색, ❌ 로그인 (!내부 이슈 : 404 로봇이 아님을 증명해야하는 화면 노출)
    {
        'name': 'digikey',
        'url': 'https://www.digikey.kr/',
        'entry': False,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/header/div[1]/div[2]/div/div[2]/div[2]/input',
        },
        'login': {},
        'user_info': {
            'user_id': 'info@olive-ems.com',
            'user_pw': 'Tvp5150am1!!'
         } 
    },
    # 14. Mouser : ❌ 검색, ❌ 로그인 (!내부 이슈 : "당신이 인간인지 확인해주세요" 문구 노출, 해결 방법 확인 필요)
    {
        'name': 'mouser',
        'url': 'https://www.mouser.kr/',
        'entry': None,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/header/div[4]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/input[1]',
        },
        'login': {},
        'user_info': {
            'user_id': 'Amypark',
            'user_pw': 'tvp5150am1'
        }
    },
    # 20. Trusted Parts : ❌ 검색 (!내부 이슈: 당신이 로봇이 아님을 확인하기 위한 필수 절차입니다. 화면 노출) 
    {
        'name': 'trusted-parts',
        'url': 'https://www.trustedparts.com/en',
        'entry': False,
        'search': {
            'selector': By.ID,
            'element': 'searchText',
        },
        'login': None
    }
]

drivers = []
num_drivers = len(sites)
print('🩵🩵🩵🩵🩵🩵🩵', len(sites))

def search_and_login(driver, search_query, index):
    driver.get(sites[index]['url'])

    print('entry', sites[index]['entry'])

    if sites[index]['entry']:
        driver.find_element(By.CSS_SELECTOR, "div.v-card__title button").click()

    # 로그인 자동화 
    if sites[index]['login']:

        print('💟💟💟💟💟💟💟💟💟💟💟💟', sites[index]['name'])

        if sites[index]['name'] == 'broker-forum':
            time.sleep(2)
            driver.find_element(By.ID, 'loginButton').click()

        if sites[index]['name'] == 'microchip-direct':
            time.sleep(2)
            driver.find_element(By.ID, 'mainMenuLoginButton').click()

        login_box = driver.find_element(sites[index]['login']['selector'][0], sites[index]['login']['element'][0])
        print('💟💟💟💟💟💟💟💟💟💟💟💟', login_box)
        login_box.send_keys(sites[index]['user_info']['user_id'])
        time.sleep(2)
        
        if sites[index]['name'] == 'ti-store':
            driver.find_element(By.ID, 'nextbutton').click()

        login_box = driver.find_element(sites[index]['login']['selector'][1], sites[index]['login']['element'][1])
        login_box.send_keys(sites[index]['user_info']['user_pw'])
        time.sleep(2)
        login_box.send_keys(Keys.RETURN)
        time.sleep(8)

        if sites[index]['name'] == 'allparts':
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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
drivers.append(driver)

while True:
    search_query = input("검색어를 입력하세요: ")

    if search_query:
        for index in range(num_drivers):
            search_and_login(drivers[0], search_query, index)

    else:
        print("검색어를 입력하지 않았습니다. 검색어를 입력해주세요.")
