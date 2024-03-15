import os
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QCheckBox, QMessageBox, QLabel, QHBoxLayout, QGridLayout
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from sites import sites
import time

def func1(site, search_query, driver, driverWait, first_code):
    if site['code'] == first_code:
        driver.get(site['url'])
    else:
        driver.execute_script("window.open('" + site['url'] + 'search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=' + search_query + "', '_blank')")
        driver.switch_to.window(driver.window_handles[-1])

    try:
    #     # 로그인 아이디/비밀번호 입력 자동화 
    #     id_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][0], site['login']['element'][0])))
    #     id_box.send_keys(site['user_info']['user_id'])

    #     pw_box = driverWait.until(EC.visibility_of_element_located((site['login']['selector'][1], site['login']['element'][1])))
    #     pw_box.send_keys(site['user_info']['user_pw'])
    #     # pw_box.send_keys(Keys.RETURN)
        search_box = driverWait.until(EC.visibility_of_element_located((site['search']['selector'], site['search']['element'])))
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    except (NoSuchElementException, AttributeError, WebDriverException) as e:
        print(f"ERROR ({site['code'], site['name']}): {e}")



def search_login_and_retry(site, search_query, driver, first_code):
    max_retries = 2
    retry_count = 0

    driverWait = WebDriverWait(driver, 20)

    while retry_count < max_retries:
        try:
            site['function'](site, search_query, driver, driverWait, first_code)
            break
        except (NoSuchElementException, AttributeError, WebDriverException) as e:
            print(f"ERROR ({site['name']}): {e}")
            retry_count += 1

    retry_count = 0

sites = [
    {
        'code': 1,
        'name': 'naver',
        'url': 'https://www.naver.com/',
        'function': func1,
        'entry': False,
        'retry': [By.ID, 'nx_query'],
        'search': {
            'selector': By.ID,
            'element': 'query',
        },
        'login': None
    },
]

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class WebAutomationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.driver = None

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.central_widget.setLayout(self.layout)
        self.setWindowTitle("Merry Christmas, Binning🩵")
        self.setGeometry(100, 100, 400, 100)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("너와의 첫 번째 크리스마스 너무 설레어🩵")
        self.search_input.setFixedHeight(30) 
        search_layout.addWidget(self.search_input)

        self.search_button = QPushButton("검색", self)
        self.search_button.setFixedWidth(60) 
        search_layout.addWidget(self.search_button)
        self.layout.addLayout(search_layout)


        site_layout = QVBoxLayout()
        self.select_all_button = QPushButton("Click Me!", self)
        self.select_all_button.setFixedWidth(100) 
        site_layout.addWidget(self.select_all_button)
        self.select_all_button.clicked.connect(self.toggle_select_all)
        self.layout.addLayout(site_layout)

        # Use this updated code to arrange checkboxes in two rows:
        self.check_boxes = []
        num_cols = 2  # Number of columns (2 in this case)
        self.checkbox_grid_layout = QGridLayout()
        for index, site in enumerate(sites):
            check_box = QCheckBox(site['name'], self)
            self.check_boxes.append(check_box)

            row = index // num_cols
            col = index % num_cols
            self.checkbox_grid_layout.addWidget(check_box, row, col)

        # Add the grid layout to the main layout
        self.layout.addLayout(self.checkbox_grid_layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                color: #333333;
            }
            QLineEdit {
                background-color:#f8f9fc;
                padding-left: 5px;
                color: #6e707e;
                border: 1px solid #cccccc;
            }
            QPushButton {
                background-color: #4e73df;
                color: white;
                font-weight: 700;
                border: 2px solid #007acc;
                border-radius: 15px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #2e59d9;
                border: 2px solid #2e59d9;
                border-radius: 15px;
            }
            # QPushButton:pressed {
            #     background-color: #004580;
            #     border: 2px solid #004580;
            # }
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

    def toggle_select_all(self):
        check_all = True
        # Check if any checkbox is unchecked; if so, set check_all to True
        for check_box in self.check_boxes:
            if not check_box.isChecked():
                check_all = False
        
        # Toggle the state of all checkboxes based on the check_all flag
        for check_box in self.check_boxes:
            check_box.setChecked(not check_all)
        # self.select_all_button.setText("전체 선택" if check_all else "전체 해제")

    def perform_search(self):
        search_query = self.search_input.text()

        selected_sites = []

        # if len(search_query) < 4:
        #     QMessageBox.critical(self, "오류", "검색어는 최소 4글자 이상이어야 합니다.")
        #     return

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
                    
                    # 전체 버튼 disabled
                    self.select_all_button.setDisabled(True)
                    self.select_all_button.setStyleSheet("background-color: #CCCCCC; color: #999999; border: 1px solid #CCCCCC")

                    for check_box in self.check_boxes:
                        check_box.setDisabled(True)
                    
                    for site in selected_sites:
                        search_login_and_retry(site, search_query, self.driver, selected_sites[0]['code'])

            else :
                selected_site = []
                driverWait = WebDriverWait(self.driver, 10)

                for index, site in enumerate(self.check_boxes):
                    if site.isChecked():
                        selected_site.append(sites[index])
                    
                if selected_site:
                    
                    for index, site in enumerate(selected_site):
                        if site['retry'] != None:
                            try:
                                self.driver.switch_to.window(self.driver.window_handles[index])
                                retry_search = driverWait.until(EC.visibility_of_element_located((site['retry'][0], site['retry'][1])))
                                self.driver.execute_script("arguments[0].value = '';", retry_search)
                                # 다시 검색할 검색어 입력 
                                retry_search.send_keys(search_query)
                                retry_search.send_keys(Keys.RETURN)

                            except (NoSuchElementException, AttributeError, WebDriverException) as e:
                                print(f"RETRY ERROR ({site['code'], site['name']}): {e}")
                                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebAutomationApp()
    window.show()
    sys.exit(app.exec())