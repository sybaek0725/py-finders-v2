import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QCheckBox, QMessageBox, QLabel, QHBoxLayout
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from sites import sites
import time

def func1(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.get(site['url'] + 'search/' + search_query)

def func2(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + 'search?key=' + search_query + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

def func3(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + 'kor/item_list.php?search_mode=1&sql_one=' + search_query + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    # try:
    #     accept_btn = driverWait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
    #     accept_btn.click()
        
    #     driver.find_element(By.CLASS_NAME, 'adi-f__meta__newsletters__cta').click()

    #     id_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0])))
    #     id_box.send_keys(site['user_info']['user_id'])

    #     pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
    #     pw_box.send_keys(site['user_info']['user_pw'])
    #     pw_box.send_keys(Keys.RETURN)
    # except (NoSuchElementException, AttributeError, WebDriverException) as e:
    #     print(f"ERROR ({site['code'], site['name']}): {e}")

def func4(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + 'part/' +  search_query + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

def func5(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + 'p/d/' + search_query + '.htm' + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

def func6(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    try:
        driver.execute_script("window.open('" + site['url'] + 'search?q=' + search_query + "', '_blank')")
        driver.switch_to.window(driver.window_handles[-1])    

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

    finally:
        # 검색 공통 로직
        ship_popup = driverWait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[3]/div/div/div[3]/button[2]')))
        ship_popup.click

def func7(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + 'search/' + search_query + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

def func8(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        id_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0])))
        id_box.send_keys(site['user_info']['user_id'])            

        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        # 비밀번호 다음에 변경하기
        driverWait.until(EC.visibility_of_element_located((By.ID, 'btnHideWeek'))).click()

        # 검색 공통 로직
        search_box = driverWait.until(EC.visibility_of_element_located((site['search']['selector'], site['search']['element'])))
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func9(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        id_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0])))
        id_box.send_keys(site['user_info']['user_id'])

        time.sleep(5)

        # 아이디 입력 후 다음 버튼
        next_btn = driver.find_element(By.XPATH, '/html/body/main/div/div/div/form/div/div[1]/ti-button//button')
        print('==========', next_btn)
        next_btn.click()

        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        # 검색 공통 로직
        search_box = driver.find_element(site['search']['selector'], site['search']['element'])
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func11(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try: 
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][2], site['login']['element'][2]))).send_keys(site['user_info']['user_num'])

        # 로그인 공통 로직 
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0]))).send_keys(site['user_info']['user_id'])            
        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        search_box = driver.find_element(site['search']['selector'], site['search']['element'])
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func12(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try: 
        # 로그인 공통 로직 
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0]))).send_keys(site['user_info']['user_id'])            
        driver.find_element(By.CLASS_NAME, 'passwordhidden').click()
        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        # 로딩 속도
        time.sleep(10)

        search_box = driver.find_element(site['search']['selector'], site['search']['element'])
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func14(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try: 
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0]))).send_keys(site['user_info']['user_id'])            
        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        # 로그인 실패 에외 처리
        if site['login']['element'][2]:
            driver.find_element(By.ID, 'submitLogin').submit()

        time.sleep(10)

        search_box = driver.find_element(site['search']['selector'], site['search']['element'])
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")
        

def func16(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        id_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0])))
        id_box.send_keys(site['user_info']['user_id'])
        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        time.sleep(15)

        # 로그인 실패 에외 처리
        if site['login']['element'][2]:
            driver.find_element(site['login']['selector'][2], site['login']['element'][2]).click()

        # 검색 공통 로직
        search_box = driver.find_element(site['search']['selector'], site['search']['element'])
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func17(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        driverWait.until(EC.visibility_of_element_located((By.ID, 'loginButton'))).click()

        # 로그인 공통 로직 
        id_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0])))
        id_box.send_keys(site['user_info']['user_id'])            

        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.submit()

        # 검색 공통 로직
        search_box = driverWait.until(EC.visibility_of_element_located((site['search']['selector'], site['search']['element'])))
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func18(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        driver.find_element(By.ID, 'mainMenuLoginButton').click()

        # 로그인 공통 로직 
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0]))).send_keys(site['user_info']['user_id'])            
        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        time.sleep(5)

        # 검색 공통 로직
        # URL 검색어 없음
        search_box = driverWait.until(EC.visibility_of_element_located((site['search']['selector'], site['search']['element'])))
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func19(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        accept_btn = driverWait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
        accept_btn.click()
        
        driver.find_element(By.CLASS_NAME, 'adi-f__meta__newsletters__cta').click()

        id_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0])))
        id_box.send_keys(site['user_info']['user_id'])

        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        # ad-web 검색 로직
        search_box = driverWait.until(EC.visibility_of_element_located((site['search']['selector'], site['search']['element'])))
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func20(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        # 사이트 진입 시 쿠키 정책 팝업 닫기
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][2], site['login']['element'][2]))).click()
        
        # 홈 > 로그인 버튼 클릭
        driverWait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/noindex[1]/header/div/div/nav/div/ul/li[5]/div/div[1]/a'))).click()

        # 로그인 팝업 창 노출
        time.sleep(5)
        
        # 로그인 팝업 창 > 쿠키 정책 팝업 닫기
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][3], site['login']['element'][3]))).click()

        # 로그인 팝업 창 > 쿠키 정책 팝업 닫기 > 이메일 입력
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0]))).send_keys(site['user_info']['user_id'])
        # 로그인 팝업 창 > 쿠키 정책 팝업 닫기 > 패드워드 입력 후 엔터
        pw = driver.find_element(site['login']['selector'][1], site['login']['element'][1])
        pw.send_keys(site['user_info']['user_pw'])
        pw.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")
    finally:
        # 쿠키 정책 팝업 닫기
        driverWait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click
        
        # # 검색 자동화
        search_box = driverWait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/div/div[1]/div[1]/div/form/div/div/input[2]')))
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # # 검색 결과 화면에서 쿠키 정책 팝업 닫기
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][2], site['login']['element'][2]))).click()

def func10(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        # 로그인 공통 로직 
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0]))).send_keys(site['user_info']['user_id'])            
        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        time.sleep(7)

        # 검색 공통 로직
        search_box = driver.find_element(site['search']['selector'], site['search']['element'])
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func13(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        # 로그인 공통 로직 
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0]))).send_keys(site['user_info']['user_id'])            
        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        time.sleep(10)

        # 검색 공통 로직
        search_box = driver.find_element(site['search']['selector'], site['search']['element'])
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

def func15(site, search_query, driver, driverWait):
    print('🩵🩵🩵🩵🩵', site['code'], site["name"])
    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])

    try:
        id_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0])))
        id_box.send_keys(site['user_info']['user_id'])            

        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])
        pw_box.send_keys(Keys.RETURN)

        system_error_popup = '/html/body/div[6]/div[2]/div/mat-dialog-container/caution-tape-modal/div/button'

        if system_error_popup: 
            driver.find_element(By.XPATH, system_error_popup).click()

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")

    finally:
        # 검색 공통 로직
        search_box = driverWait.until(EC.visibility_of_element_located((site['search']['selector'], site['search']['element'])))
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

# def func21(site, search_query, driver):
#     print('🩵🩵🩵🩵🩵', site['code'], site["name"]) 
#     driver.execute_script("window.open('" + site['url'] + "', '_blank')")
#     driver.switch_to.window(driver.window_handles[-1])

# def func22(site, search_query, driver):
#     print('🩵🩵🩵🩵🩵', site['code'], site["name"])
#     driver.execute_script("window.open('" + site['url'] + "', '_blank')")
#     driver.switch_to.window(driver.window_handles[-1])
        
def search_login_and_retry(site, search_query, driver):
    max_retries = 2
    retry_count = 0

    driverWait = WebDriverWait(driver, 20)

    while retry_count < max_retries:
        try:
            site['function'](site, search_query, driver, driverWait)
            break
        except (NoSuchElementException, AttributeError, WebDriverException) as e:
            print(f"ERROR ({site['name']}): {e}")
            retry_count += 1

    retry_count = 0

sites = [
    {
        'code': 1,
        'name': 'findchips',
        'url': 'https://www.findchips.com/',
        'function': func1,
        'entry': False,
        'retry': [By.XPATH, '/html/body/header/div/div[2]/form/span/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[2]/div/div/div[1]/div/form/span/input',
        },
        'login': None
    },
    {
        'code': 2,
        'name': 'find-ic',
        'url': 'https://www.findic.kr/',
        'function': func2,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[2]/div/div[2]/form/input[1]'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[4]/div[2]/form/input[1]',
        },
        'login': None
    },
    {
        'code': 3,
        'name': 'partsner',
        'url': 'http://www.partsner.com/',
        'function': func3,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[1]/div[1]/div/ul[2]/li[2]/span/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[2]/div[1]/div/ul/li[2]/input',
        },
        'login': None
    },
    {
        'code': 4,
        'name': 'digi-parts',
        'url': 'https://www.digipart.com/',
        'function': func4,
        'entry': False,
        'retry': [By.XPATH, '/html/body/nav/div/div[2]/form/div/div/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[1]/div/div[1]/form/div/div/input',
        },
        'login': None
    },
    # {
    #     'code': 5,
    #     'name': 'hk-inventory',
    #     'url': 'https://www.hkinventory.com/',
    #     'function': func5,
    #     'entry': False,
    #     'retry': [By.XPATH, '/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/center/div/table/tbody/tr/td/div[2]/form/div[1]/input[1]'],
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/center/div[1]/div[1]/form/div[1]/input[1]',
    #     },
    #     'login': None
    # },
    {
        'code': 6,
        'name': 'lcsc',
        'url': 'https://www.lcsc.com/',
        'function': func6,
        'entry': True,
        'retry': [By.XPATH, '/html/body/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/input',
        },
        'login': None
    },
    # {
    #     'code': 7,
    #     'name': 'trusted-parts',
    #     'url': 'https://www.trustedparts.com/en/',
    #     'function': func7,
    #     'entry': False,
    #     'search': {
    #         'selector': By.ID,
    #         'element': 'searchText',
    #     },
    #     'login': None
    # },
    {
        'code': 8,
        'name': 'allparts',
        'url': 'https://www.allparts.co.kr/',
        'function': func8,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[3]/div[2]/form/div/input[1]'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[1]/div[3]/div/input',
        },
        'login': {  
            'selector': [By.ID, By.ID],
            'element': ['user_id', 'pswd'],
        },
        'user_info': {
            'user_id': 'mworksk2',
            'user_pw': 'tvp5150am1pbsr'
        },
    },
    # xpath 에러남
    {
        'code': 9,
        'name': 'ti-store',
        'url': 'https://login.ti.com/as/authorization.oauth2?response_type=code&scope=openid%20email%20profile&client_id=DCIT_ALL_WWW-PROD&state=ASyLnI6G2yrRzK62u53IkdH9_T0&redirect_uri=https%3A%2F%2Fwww.ti.com%2Foidc%2Fredirect_uri%2F&nonce=EB0zAM0EHXE83JqVK1Bagm3Wa84cROtpvDQ23RP6LrY&response_mode=form_post',
        'function': func9,
        'entry': False,
        'retry': [By.XPATH, '/html/body/header/div[3]/div[2]/div[1]/div/div/div/div/div/div[1]/input'],
        'search': {
            'selector': By.CSS_SELECTOR,
            'element': 'div#searchboxheader input',
        },
        'login': {  
            'selector': [By.ID, By.XPATH], 
            'element': ['username', '/html/body/main/div/div/div/form/div/div[2]/ti-password/input'],
        },
        'user_info': {
            'user_id': 'INFO@OLIVE-EMS.COM',
            'user_pw': 'Tvp5150am1!!'
        },
    },
    {
        'code': 10,
        'name': 'ssdi-power',
        'url': 'https://ssdi-power.com/customer/account/login/',
        'function': func10,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[2]/header/div[2]/div/section/div/section[1]/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[2]/header/div[2]/div/section/div/section[1]/input',
        },
        'login': {
            'selector': [By.ID, By.ID],
            'element': ['email', 'pass'],
        },
        'user_info': {
            'user_id': 'info@olive-ems.com',
            'user_pw': 'Tvp5150am1!!',
        }
    },
    {
        'code': 11,
        'name': 'net-components', 
        'url': 'https://m.netcomponents.com/ko/account/login',
        'function': func11,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/form/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/span/input'],
        'search': {
            'selector': By.CLASS_NAME,
            'element': 'searched-part',
        },
        'login': {  
            'selector': [By.ID, By.ID, By.ID],
            'element': ['UserName', 'Password', 'AccountNumber'],
        },
        'user_info': {
            'user_num': '820990',
            'user_id': 'mworksk',
            'user_pw': 'Tvp5150am1!!'
        },
    },
    {
        'code': 12,
        'name': 'ic-source',
        'url': 'https://icsource.com/Home/Index.aspx',
        'function': func12,
        'entry': False,
        'retry': [By.XPATH, '/html/body/form/div[15]/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/div/div[3]/table/tbody/tr/td[2]/div[1]/div/span/input[1]'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/form/div[15]/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/div/div[3]/table/tbody/tr/td[2]/div[1]/div/span/input[1]',
        },
        'login': {  
            'selector': [By.XPATH, By.CLASS_NAME], 
            'element': ['/html/body/form/div[6]/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/input', 'password'],
        },
        'user_info': {
            'user_id': 'mworks',
            'user_pw': 'Tvp5150am1!!'
        },
    },
    {
        'code': 13,
        'name': 'arrow',
        'url': 'https://www.arrow.com/ko-kr/login?gotoSplash=true&url=',
        'function': func13,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[1]/header/div[2]/div[1]/div[1]/div/div[1]/form/div/input[1]'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[1]/header/div/div[1]/div[1]/div/div[1]/form/div/input[1]',
        },
        'login': {  
            'selector': [By.ID, By.ID], 
            'element': ['username', 'password'],
        },
        'user_info': {
            'user_id': 'mjang@microworks.co.kr',
            'user_pw': 'Tvp5150am1pbsr!'
        },
    },
    {
        'code': 14,
        'name': 'element14',
        'url': 'https://kr.element14.com/webapp/wcs/stores/servlet/LogonForm?myAcctMain=1&catalogId=15001&storeId=10187&langId=-9&URL=https%3A%2F%2Fkr.element14.com%2F',
        'function': func14,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[3]/div[1]/header/div[2]/div[2]/form/div/div/div[1]/div[2]/input[2]'],
        'search': {
            'selector': By.ID,
            'element': 'SimpleSearchForm_SearchTerm',
        },
        'login': {  
            'selector': [By.XPATH, By.XPATH, By.XPATH], 
            'element': ['/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[3]/input', '/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[5]/input', '/html/body/div[4]/div/main/div[1]/div[2]/ul/li/span'],
        },
        'user_info': {
            'user_id': 'Steelan',
            'user_pw': 'tvp5150am1'
        },
    },
    {
        'code': 15,
        'name': 'verical',
        'url': 'https://www.verical.com/sign-in?return=%2F',
        'function': func15,
        'entry': False,
        'retry': [By.XPATH, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/verical-header/div/div[2]/div[1]/div/div[2]/div[2]/search-form/form/div[1]/div/mat-form-field/div/div[1]/div[1]/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/verical-header/div/div[2]/div[1]/div/div[2]/div[2]/search-form/form/div[1]/div/mat-form-field/div/div[1]/div[1]/input',
        },
        'login': {  
            'selector': [By.XPATH, By.XPATH, By.XPATH], 
            'element': ['/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[1]/div/div[1]/div/input', '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[2]/div/div[1]/div/input', ''],
        },
        'user_info': {
            'user_id': 'mjang@microworks.co.kr',
            'user_pw': 'Tvp5150am1pbsr!'
        },
    },
    {
        'code': 16,
        'name': 'chip-one-stop',
        'url': 'https://www.chip1stop.com/KOR/ko/login',
        'function': func16,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[1]/header/div[1]/div[2]/div/form/div[2]/input[1]'],
        'search': {
            'selector': By.ID,
            'element': 'headerKeywordSearch',
        },
        'login': {  
            'selector': [By.ID, By.ID, By.XPATH], 
            'element': ['j_idt1348:loginId', 'j_idt1348:password', '/html/body/div[1]/main/form/div[1]/button'],
        },
        'user_info': {
            'user_id': 'mworksk',
            'user_pw': 'mworksk123'
        },
    },
    {
        'code': 17,
        'name': 'microchip-direct',
        'url': 'https://www.microchipdirect.com/',
        'function': func17,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[8]/div/div[1]/div[2]/div/div/div/div[1]/nav[1]/ul[2]/div/div/div[1]/div/input'],
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
    {
        'code': 18,
        'name': 'broker-forum',
        'url': 'https://www.brokerforum.com/',
        'function': func18,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/form/div[2]/div[1]/div/input'],
        'search': {
            'selector': By.ID,
            'element': 'headerSB_SearchCriteria_originalFullPartNumber',
        },
        'login': {  
            'selector': [By.ID, By.ID], 
            'element': ['Session_Username', 'Session_Password'],
        },
        'user_info': {
            'user_id': 'mworksap',
            'user_pw': 'Tvp5150am1!!'
        },
    },
    {
        'code': 19,
        'name': 'ad-web',
        'url': 'https://www.analog.com/en/index.html',
        'function': func19,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div[2]/div[1]/div[2]/form/div/span/input[2]'],
        'search': {
            'selector': By.ID,
            'element': 'text-global-search',
        },
        'login': {  
            'selector': [By.ID, By.ID], 
            'element': ['signInName', 'password'],
        },
        'user_info': {
            'user_id': 'bmselec@bmselec.co.kr',
            'user_pw': 'Tvp5150am1!!'
        },
    },
    {
        'code': 20,
        'name': 'maxim-web',
        'url': 'https://www.maximintegrated.com/en/storefront/storefront.html',
        'function': func20,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div[2]/div[2]/form/div/div[1]/input[2]'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[4]/div[2]/div/div[3]/div/div[1]/div[1]/div/form/div/div/input[2]',
        },
        'login': {  
            'selector': [By.XPATH, By.XPATH, By.XPATH, By.XPATH], 
            'element': ['/html/body/div[3]/div[1]/div/div[2]/div/div/form/div[3]/div[1]/input', '/html/body/div[3]/div[1]/div/div[2]/div/div/form/div[3]/div[2]/input', '/html/body/div[20]/div[2]/div/div[1]/div/div[2]/div/button[3]', '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/button[3]'],
        },
        'user_info': {
            'user_id': 'apark@microworks.co.kr',
            'user_pw': 'Tvp5150am1!!'
        },
    },
    # {
    #     'code': 21,
    #     'name': 'digikey',
    #     'url': 'https://www.digikey.kr/',
    #     'function': func21,
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/header/div[1]/div[2]/div/div[2]/div[2]/input',
    #     },
    #     'login': {  
    #         'selector': ['', ''], 
    #         'element': ['', ''],
    #     },
    #     'user_info': {
    #         'user_id': 'info@olive-ems.com',
    #         'user_pw': 'Tvp5150am1!!'
    #     },
    # },
    # {
    #     'code': 22,
    #     'name': 'mouser',
    #     'url': 'https://www.mouser.kr/MyAccount/MouserLogin',
    #     'function': func22,
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/header/form/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/input[1]',
    #     },
    #     'login': {  
    #         'selector': [By.XPATH, By.XPATH],
    #         'element': ['/html/body/main/div/div/div/div[2]/div/div[1]/div[4]/form/div[1]/input', '/html/body/main/div/div/div/div[2]/div/div[1]/div[4]/form/div[2]/input']
    #     },
    #     'user_info': {
    #         'user_id': 'Amypark',
    #         'user_pw': 'tvp5150am1'
    #     },
    # },
    # {
    #     'code': 23,
    #     'name': 'digikey',
    #     'url': 'https://www.digikey.kr/',
    #     'function': func21,
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '/html/body/header/div[1]/div[2]/div/div[2]/div[2]/input',
    #     },
    #     'login': {  
    #         'selector': [By.XPATH, By.XPATH], 
    #         'element': ['', ''],
    #     },
    #     'user_info': {
    #         'user_id': 'ekim@microworks.co.kr',
    #         'user_pw': 'tvp5150am1!!'
    #     },
    # },
    # {
    #     'code': 24,
    #     'name': 'mouser',
    #     'url': 'https://www.mouser.kr/MyAccount/MouserLogin',
    #     'function': func22,
    #     'entry': False,
    #     'search': {
    #         'selector': By.XPATH,
    #         'element': '',
    #     },
    #     'login': {  
    #         'selector': [By.XPATH, By.XPATH],
    #         'element': ['', '']
    #     },
    #     'user_info': {
    #         'user_id': 'oliveems',
    #         'user_pw': 'Tvp5150am1!!'
    #     },
    # },
]

class WebAutomationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.driver = None

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.title_label = QLabel("구매팀 소싱 포털", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(self.title_label)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("검색어를 입력하세요")
        search_layout.addWidget(self.search_input)

        self.search_button = QPushButton("검색", self)
        search_layout.addWidget(self.search_button)
        self.layout.addLayout(search_layout)

        self.central_widget.setLayout(self.layout)
        self.setWindowTitle("웹 자동화 애플리케이션")
        self.setGeometry(100, 100, 400, 100)

        self.image_label = QLabel(self)
        image_pixmap = QPixmap("logo.png")  
        self.image_label.setPixmap(image_pixmap)
        self.layout.addWidget(self.image_label)

        self.check_boxes = [] 
        for site in sites:
            check_box = QCheckBox(site['name'], self)
            check_box.setChecked(True) 
            self.layout.addWidget(check_box)
            self.check_boxes.append(check_box)

        self.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border: 2px solid #007acc;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0058a4;
                border: 2px solid #0058a4;
            }
            QPushButton:pressed {
                background-color: #004580;
                border: 2px solid #004580;
            }
        """)

        for check_box in self.check_boxes:
            check_box.stateChanged.connect(self.checkbox_state_changed)

        self.search_button.clicked.connect(self.perform_search)
        self.search_input.returnPressed.connect(self.perform_search)

    def checkbox_state_changed(self, state):
        checked_boxes = []  
        
        for i, check_box in enumerate(self.check_boxes):
            if check_box.isChecked():
                checked_boxes.append(check_box.text())

    def perform_search(self):
        search_query = self.search_input.text()

        selected_sites = []

        if len(search_query) < 4:
            QMessageBox.critical(self, "오류", "검색어는 최소 4글자 이상이어야 합니다.")
            return

        if not any(site.isChecked() for site in self.check_boxes):
            QMessageBox.critical(self, "오류", "적어도 하나의 사이트를 선택해야 합니다.")
            return

        if search_query.lower() == 'close': 
            self.driver.quit()
            self.driver = None
        else:
            if self.driver is None:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_experimental_option("detach", True)
                chrome_options.add_argument('--disable-blink-features=AutomationControlled')
                chrome_options.add_argument("--disable-extensions")
                chrome_options.add_argument("--start-maximized")
                self.driver = webdriver.Chrome(options=chrome_options)

                for index, site in enumerate(self.check_boxes):
                    if site.isChecked():
                        selected_sites.append(sites[index])

                if search_query and selected_sites:
                    for site in selected_sites:
                        search_login_and_retry(site, search_query, self.driver)
            else :
                for index, site in enumerate(self.check_boxes):
                    if site.isChecked():
                        selected_site = sites[index]
                        self.driver.switch_to.window(self.driver.window_handles[index])
                        
                        
                        retry_search = self.driver.find_element(selected_site['retry'][0], selected_site['retry'][1])
                        self.driver.execute_script("arguments[0].value = '';", retry_search)
                        retry_search.send_keys(search_query)
                        retry_search.send_keys(Keys.RETURN)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebAutomationApp()
    window.show()
    sys.exit(app.exec())