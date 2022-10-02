#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import nltk

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--remote-debugging-port=9222")

try:
  driver = webdriver.Chrome(options=options)
  driver.get("https://www.instagram.com")
  time.sleep(2)
  #id.pwd 입력
  _id = driver.find_element(By.NAME,"username")
  _id.send_keys("mao.wncloset")
  time.sleep(2)
  _pwd = driver.find_element(By.NAME, 'password')
  _pwd.send_keys("Mmqwer1234!!")
  time.sleep(2)
  #각 버튼 클릭
  driver.find_element(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF').click()
  time.sleep(5)
  #키워드 검색하기
  driver.get('https://www.instagram.com/explore/tags/' + '사과' + '/')
  time.sleep(5)
  #첫번째 게시물 열기
  driver.find_element(By.CLASS_NAME, '_aabd._aa8k._aanf').click()
  time.sleep(5)
  #여러 게시물에서 해시태그 크롤링
  results = []
  count = 1
  for i in range(count):
      data = driver.find_elements(By.CSS_SELECTOR, 'span._aacl._aaco._aacu._aacx._aad7._aade > a')
      time.sleep(3)
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
  topWord = text.vocab().most_common(5)

  assert s.is_displayed() is True
  print("ok\n")
  print(topWord)
except Exception as ex:
  print(ex)

driver.quit()
