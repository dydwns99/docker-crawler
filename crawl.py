from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import nltk

# keyword = transWord()
# 1. 웹페이지 열기
try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-loggin"])
    driver = webdriver.Chrome(options=options)

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
    a = driver.find_element(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF')
    a.click()
    time.sleep(5)
    # login_button = driver.find_element(By.CLASS_NAME, '_acan._acap._acas').click()
    # time.sleep(5)
    # driver.find_element(By.CLASS_NAME, '_ac8f').click()
    # time.sleep(3)

    # driver.find_element(By.CLASS_NAME, '_a9--._a9_1').click()
    # time.sleep(3)

    # 4. 키워드 검색하기
    # keyword = 'ootd'
    driver.get('https://www.instagram.com/explore/tags/' + 'apple' + '/')
    time.sleep(5)

    # # 5. 첫번째 게시물 열기
    # a = driver.find_element(By.CLASS_NAME, '_aabd._aa8k._aanf')
    # time.sleep(5)
    # #
    # # 6. 여러 게시물에서 해시태그 크롤링
    # results = []
    # count = 3
    # for i in range(count):
    #     data = driver.find_elements(By.CSS_SELECTOR, 'span._aacl._aaco._aacu._aacx._aad7._aade > a')
    #     time.sleep(2)
    #     for j in range(len(data)):
    #         results.append(data[j].text.replace("#", ""))  # '#'제거
    #
    #     if (i + 1) % 3 == 0:
    #         print("{}번째 게시물 완료".format(i + 1))
    #     driver.find_element(By.CLASS_NAME, '_aaqg._aaqh').click()
    #     time.sleep(3)
    #
    # results_str = " ".join(results)  # 결과값 list to string
    # tokens = results_str.split(" ")  # 각 단어별로 떼어 내서
    # text = nltk.Text(tokens)  # text에 저장하고
    # print(text)
    # topWord = text.vocab().most_common(5)  # 가장 많이 등장하는 5개의 단어를 추려낸다.


    assert a.is_displayed() is True
    print("ok")
    # print(topWord)
except Exception as ex:
    print(ex)


