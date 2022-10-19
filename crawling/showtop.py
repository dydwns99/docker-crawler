from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import nltk

def showTop(word):

<<<<<<< HEAD
    # 1. 웹페이지 열기
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    driver.maximize_window()
    time.sleep(1)

    # 2. id, pwd 입력
    _id = driver.find_element(By.NAME, 'username')
    _id.send_keys("mao.wncloset")
    time.sleep(2)

    _pwd = driver.find_element(By.NAME, 'password')
    _pwd.send_keys("Mmqwer1234!!")
    time.sleep(2)

    # 3. 각 버튼 클릭
    login_button = driver.find_element(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF').click()
    time.sleep(5)

    # driver.find_element(By.CLASS_NAME, 'sqdOP.yWX7d.y3zKF').click()
    # time.sleep(3)
=======
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--remote-debugging-port=9222")
>>>>>>> 68f5a7e71f3a82582ff08d66a46f815bb7f90a81

    try:

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.instagram.com")
        time.sleep(3)
        #id.pwd 입력
        _id = driver.find_element(By.NAME,"username")
        _id.send_keys("mao.wncloset")
        time.sleep(2)
        _pwd = driver.find_element(By.NAME, 'password')
        _pwd.send_keys("Mmqwer1234!!")
        time.sleep(2)
        #각 버튼 클릭
        a = driver.find_element(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF')
        time.sleep(1)
        a.click()
        time.sleep(10)
        #키워드 검색하기
        driver.get('https://www.instagram.com/explore/tags/' + word + '/')
        time.sleep(5)
        #첫번째 게시물 열기
        b = driver.find_element(By.CLASS_NAME, '_aabd._aa8k._aanf')
        time.sleep(1)
        b.click()
        time.sleep(5)
        #여러 게시물에서 해시태그 크롤링
        results = []
        count = 15
        for i in range(count):
            data = driver.find_elements(By.CSS_SELECTOR, 'span._aacl._aaco._aacu._aacx._aad7._aade > a')
            time.sleep(6)
            # '#'제거
            for j in range(len(data)):
                results.append(data[j].text.replace("#", ""))
            if (i + 1) % 3 == 0:
                print("{}번째 게시물 완료".format(i + 1))
            s = driver.find_element(By.CLASS_NAME, '_aaqg._aaqh')
            s.click()
            time.sleep(3)
        #결과값 list to string
        results_str = " ".join(results)
        #각 단어별로 떼어내서
        tokens = results_str.split(" ")
        #text에 저장하고
        text = nltk.Text(tokens)
        #가장 많이 등장하는 5개의 단어를 추려낸다.
        topword = text.vocab().most_common(5)

        assert s.is_displayed() is True
        print("ok\n")
        print(topword)
    except Exception as ex:
        print(ex)

    #driver.quit()

    return topword
