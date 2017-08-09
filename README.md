# crawl_douban_comments
爬取豆瓣战狼短评，并使用wordcloud展示
## 说明:
- crawl_raw.py 爬取短评
- segment.py 分词
- draw.py 绘制
## 注意:
- selenium使用Chrome浏览器，可自行修改 (crawler/crawler.py 21行)
- 需要在 crawler/crawler.py 的 login 函数里填入用户名和密码
- 运行crawl_raw.py如果出现验证码需自行输入然后手动登录
## 图片示例:
![avatar](https://github.com/SenL1997/crawl_douban_comments/raw/master/image/Figure.png)
![avatar](https://github.com/SenL1997/crawl_douban_comments/raw/master/image/Figure_1.png)