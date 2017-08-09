import random
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time

Agent = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'
]

agent = random.choice(Agent)
session = requests.session()


def login(session):
    driver = webdriver.Chrome()
    driver.get('https://www.douban.com/accounts/login?source=movie')
    elem = driver.find_element_by_id('email')
    elem.send_keys('***')
    elem = driver.find_element_by_id('password')
    elem.send_keys('***')
    try:
        elem = driver.find_element_by_id('captcha_field')
        # text = input()
        # elem.send_keys(text)
        # elem.send_keys(Keys.ENTER)
        time.sleep(20)
    except NoSuchElementException:
        elem.send_keys(Keys.ENTER)
    cookies = {}
    for s in driver.get_cookies():
        cookies[s['name']] = s['value']
    requests.utils.add_dict_to_cookiejar(session.cookies, cookies)
    driver.close()


def download_and_parse(url, session, agent):
    headers = {
        'User-Agent': agent
    }
    response = session.get(url, headers=headers)
    html = BeautifulSoup(response.text, 'lxml')
    commentsList = html.find('div', {'class': 'mod-bd', 'id': 'comments'}).find_all('div', {'class': 'comment-item'})
    comments = []
    for item in commentsList:
        comment = item.find('p').text
        comments.append(comment.strip())
    return comments


if __name__ == '__main__':
    login(session)
    URL = 'https://movie.douban.com/subject/26363254/comments?start={}&limit=20&sort=new_score&status=P'
    url = URL.format(0)
    for comment in download_and_parse(url, session, agent=agent):
        print(comment)
