from crawler import crawler
import codecs
from multiprocessing import Process
import time
import random
import requests

Agent = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'
]


class Crawler(Process):
    def __init__(self, session, file_name, begin, end):
        super(Crawler, self).__init__()
        self.session = session
        self.begin = begin
        self.end = end
        self.file_name = file_name
        self.agent = random.choice(Agent)

    def run(self):
        URL = 'https://movie.douban.com/subject/26363254/comments?start={}&limit=20&sort=new_score&status=P'
        crawler.login(self.session)
        with codecs.open(self.file_name, 'wb', encoding='utf-8') as f:
            for i in range(self.begin, self.end, 20):
                url = URL.format(i)
                try:
                    for comment in crawler.download_and_parse(url, self.session, self.agent):
                        f.write('{}{}'.format(comment, '\r\n'))
                except AttributeError as err:
                    print(err)
                    crawler.login(self.session)
                time.sleep(random.randint(5, 10))
                print(i)

if __name__ == '__main__':
    crawl_1 = Crawler(requests.session(), 'comments_1.txt', 0, 3000)
    crawl_2 = Crawler(requests.session(), 'comments_2.txt', 3000, 6000)
    crawl_1.start()
    time.sleep(20)
    crawl_2.start()
    crawl_1.join()
    crawl_2.join()
