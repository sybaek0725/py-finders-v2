from selenium.webdriver.common.by import By


sites = [
    {
        'code': 1,
        'name': 'findchips',
        'url': 'https://www.findchips.com/',
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
        'entry': False,
        'retry': [By.XPATH, '/html/body/nav/div/div[2]/form/div/div/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[1]/div/div[1]/form/div/div/input',
        },
        'login': None
    },
    {
        'code': 5,
        'name': 'hk-inventory',
        'url': 'https://www.hkinventory.com/',
        'driver': None,
        'entry': False,
        'retry': [By.XPATH, '/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/center/div/table/tbody/tr/td/div[2]/form/div[1]/input[1]'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div[1]/center/div[1]/div[1]/form/div[1]/input[1]',
        },
        'login': None
    },
    {
        'code': 6,
        'name': 'lcsc',
        'url': 'https://www.lcsc.com/',
        'driver': None,
        'entry': True,
        'retry': [By.XPATH, '/html/body/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/input',
        },
        'login': None
    },
    {
        'code': 7,
        'name': 'trusted-parts',
        'url': 'https://www.trustedparts.com/en/',
        'driver': None,
        'entry': False,
        'search': {
            'selector': By.ID,
            'element': 'searchText',
        },
        'login': None
    },
    {
        'code': 8,
        'name': 'allparts',
        'url': 'https://www.allparts.co.kr/',
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
        'entry': False,
        'retry': [By.XPATH, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/verical-header/div/div[2]/div[1]/div/div[2]/div[2]/search-form/form/div[1]/div/mat-form-field/div/div[1]/div[1]/input'],
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/home-page/div/div[2]/div/div/div[2]/search-form/form/div[1]/div/mat-form-field/div/div[1]/div[1]/input',
        },
        'login': {  
            'selector': [By.XPATH, By.XPATH], 
            'element': ['/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[1]/div/div[1]/div/input', '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[2]/div/div[1]/div/input'],
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
        'driver': None,
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
    {
        'code': 21,
        'name': 'digikey',
        'url': 'https://www.digikey.kr/',
        'driver': None,
        'entry': False,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/header/div[1]/div[2]/div/div[2]/div[2]/input',
        },
        'login': {  
            'selector': ['', ''], 
            'element': ['', ''],
        },
        'user_info': {
            'user_id': 'info@olive-ems.com',
            'user_pw': 'Tvp5150am1!!'
        },
    },
    {
        'code': 22,
        'name': 'mouser',
        'url': 'https://www.mouser.kr/MyAccount/MouserLogin',
        'driver': None,
        'entry': False,
        'search': {
            'selector': By.XPATH,
            'element': '/html/body/header/form/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/input[1]',
        },
        'login': {  
            'selector': [By.XPATH, By.XPATH],
            'element': ['/html/body/main/div/div/div/div[2]/div/div[1]/div[4]/form/div[1]/input', '/html/body/main/div/div/div/div[2]/div/div[1]/div[4]/form/div[2]/input']
        },
        'user_info': {
            'user_id': 'Amypark',
            'user_pw': 'tvp5150am1'
        },
    },
    #digikey, mouser 계정 다른 것도 추가 예정 
]