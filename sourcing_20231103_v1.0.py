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
from sites import sites
import time

def search_and_login(site, search_query, driver):
    driver.get(site['url'])
    driverWait = WebDriverWait(driver, 15)

    # 진입 팝업
    if site['name'] == 'lcsc':
        driver.find_element(By.CSS_SELECTOR, 'div.v-card__title button').click()

    if site['name'] == 'maxim-web':
        # 사이트 진입 시 쿠키 정책 팝업 닫기
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][2], site['login']['element'][2]))).click()
        # driver.find_element(By.XPATH, '/html/body/div[20]/div[2]/div/div[1]/div/div[2]/div/button[3]').click()
        
        # 홈 > 로그인 버튼 클릭
        driverWait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/noindex[1]/header/div/div/nav/div/ul/li[5]/div/div[1]/a'))).click()
        # driver.find_element(By.XPATH, '/html/body/div[4]/noindex[1]/header/div/div/nav/div/ul/li[5]/div/div[1]/a').click()

        # 로그인 팝업 창 노출
        time.sleep(12)

        # 홈 창에서 로그인 팝업 창으로 전환 로직
        parent_window = driver.current_window_handle
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[1])

        time.sleep(10)

    # 로그인 자동화 
    if site['login']:
        # 로그인 창 진입
        if site['name'] == 'broker-forum':
            driver.find_element(By.ID, 'mainMenuLoginButton').click()
        elif site['name'] == 'microchip-direct':
            driverWait.until(EC.visibility_of_element_located((By.ID, 'loginButton'))).click()
        
        # 계정 번호 입력
        if site['name'] == 'net-components':
            driverWait.until(EC.visibility_of_element_located((site['login']['selector'][2], site['login']['element'][2]))).send_keys(site['user_info']['user_num'])

        # 쿠키 정책 팝업
        if site['name'] == 'ad-web':
            accept_btn = driverWait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            accept_btn.click()
            driver.find_element(By.CLASS_NAME, 'adi-f__meta__newsletters__cta').click()

        if site['name'] == 'maxim-web':
            # 로그인 팝업 창 > 쿠키 정책 팝업 닫기
            driverWait.until(EC.visibility_of_element_located((site['login']['selector'][3], site['login']['element'][3]))).click()

        # 아이디 입력 
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0]))).send_keys(site['user_info']['user_id'])
        
        # 비밀번호
        # 비밀번호 창 진입
        if site['name'] == 'ti-store':
            driver.find_element(By.ID, 'nextbutton').click()
        if site['name'] == 'ic-source':
            driver.find_element(By.CLASS_NAME, 'passwordhidden').click()

        # 비밀번호 입력
        pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
        pw_box.send_keys(site['user_info']['user_pw'])

        # 비밀번호 입력한 상태에서 엔터
        if site['name'] == 'microchip-direct':
            pw_box.submit()
        else:
            pw_box.send_keys(Keys.RETURN)
        
        # 다음에 변경하기 팝업
        if site['name'] == 'allparts':
            driverWait.until(EC.visibility_of_element_located((By.ID, 'btnHideWeek'))).click()

        # 로그인 실패 예외 처리
        if site['name'] == 'chip-one-stop' and site['login']['element'][2]:
            driver.find_element(site['login']['selector'][2], site['login']['element'][2]).click()
        elif site['name'] == 'element14' and site['login']['element'][2]:
            driver.find_element(By.ID, 'submitLogin').submit()

        time.sleep(10)


    # 검색 자동화 
    if site['name'] == 'ad-web':
        search_box = driverWait.until(EC.visibility_of_element_located((site['search']['selector'], site['search']['element'])))
    else:
        if site['name'] == 'maxim-web':
        # 로그인 완료 후 홈 화면으로 전환
            driver.switch_to.window(parent_window)
            # 쿠키 정책 팝업 닫기
            driverWait.until(EC.visibility_of_element_located((site['login']['selector'][2], site['login']['element'][2]))).click()
        
        search_box = driver.find_element(site['search']['selector'], site['search']['element'])

    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    if site['name'] == 'maxim-web':
        # 검색 결과 화면에서 쿠키 정책 팝업 닫기
        driverWait.until(EC.visibility_of_element_located((site['login']['selector'][2], site['login']['element'][2]))).click()
        
def search_login_and_retry(site, search_query, driver):
    max_retries = 2
    retry_count = 0
    while retry_count < max_retries:
        try:
            search_and_login(site, search_query, driver)
            break
        except (NoSuchElementException, AttributeError, WebDriverException) as e:
            print(f"ERROR ({site['name']}): {e}")
            retry_count += 1

    driver.execute_script("window.open('" + site['url'] + "', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])
    retry_count = 0


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

        # 재 검색 시나리오 X
        # self.search_button.clicked.connect(self.perform_search)
        # self.search_input.returnPressed.connect(self.perform_search)

        # 재 검색 시나리오 O
        self.search_button.clicked.connect(self.search_by_keyword)
        self.search_input.returnPressed.connect(self.search_by_keyword) 

    def checkbox_state_changed(self, state):
        checked_boxes = []  
        
        for i, check_box in enumerate(self.check_boxes):
            if check_box.isChecked():
                checked_boxes.append(check_box.text())

    # def perform_search(self):
    #     search_query = self.search_input.text()
    #     selected_sites = [] 

    #     if len(search_query) < 4:
    #         QMessageBox.critical(self, "오류", "검색어는 최소 4글자 이상이어야 합니다.")
    #         return

    #     if not any(site.isChecked() for site in self.check_boxes):
    #         QMessageBox.critical(self, "오류", "적어도 하나의 사이트를 선택해야 합니다.")
    #         return

    #     if search_query.lower() == 'close': 
    #         self.driver.quit()
    #         self.driver = None
    #     else:
    #         if self.driver is None:
    #             chrome_options = webdriver.ChromeOptions()
    #             chrome_options.add_experimental_option("detach", True)
    #             chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #             chrome_options.add_argument("--disable-extensions")
    #             chrome_options.add_argument("--start-maximized")
    #             self.driver = webdriver.Chrome(options=chrome_options)

    #             for index, site in enumerate(self.check_boxes):
    #                 if site.isChecked():
    #                     selected_sites.append(sites[index])

    #             if search_query and selected_sites:
    #                 for site in selected_sites:
    #                     search_login_and_retry(site, search_query, self.driver)
    #         else :
    #             for index, site in enumerate(self.check_boxes):
    #                 if site.isChecked():
    #                     selected_site = sites[index]
    #                     self.driver.switch_to.window(self.driver.window_handles[index])
    #                     retry_search = self.driver.find_element(selected_site['retry'][0], selected_site['retry'][1])
    #                     self.driver.execute_script("arguments[0].value = '';", retry_search)
    #                     retry_search.send_keys(search_query)
    #                     retry_search.send_keys(Keys.RETURN)

    def search_by_keyword(self):
        # while True:
        search_query = self.search_input.text()

        if len(search_query) < 4:
            QMessageBox.critical(self, "오류", "검색어는 최소 4글자 이상이어야 합니다.")
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

                if search_query:
                    for site in sites:
                        search_login_and_retry(site, search_query, self.driver)                 
            else:
                length = len(sites)
                
                for i in range(length):
                    self.driver.switch_to.window(self.driver.window_handles[i])
                    retry_search = self.driver.find_element(sites[i]['retry'][0], sites[i]['retry'][1])
                    self.driver.execute_script("arguments[0].value = '';", retry_search)
                    retry_search.send_keys(search_query)
                    retry_search.send_keys(Keys.RETURN)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebAutomationApp()
    window.show()
    sys.exit(app.exec())