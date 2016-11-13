# -*- coding: utf-8 -*
import feedparser
import MySQLdb
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'Xuhuairuogu',
        db = 'djangodb',
        charset='utf8'
)
cur = conn.cursor()

url_list = ["http://www.typeisbeautiful.com/feed/typechat/","http://songshuhui.net/feed","https://xbeta.info/feed","http://pansci.tw/feed","http://www.geekfan.net/feed/","http://xianguo.com/service/dailyshare"]
#,"http://scipark.net/feed"
for url in url_list:
    feed = feedparser.parse(url)
    lists = feed.entries
    for i in lists:
        try:
            time_format = i.published_parsed
            title = i.title
            publisher = i.author
            pub_date = time.strftime("%Y-%m-%d %X",time_format)
            url = i.id
            string = i.summary
            if "<p>" in string:
                string = string.replace('\n',"")
                com = re.compile(r'<p>(.+?)</p>')
                match = com.findall(string)
                body = match[0]
                body = body.replace('</a>', '')
                com2 = re.compile('<a .+?>')
                match = com2.findall(string)
                for i in match:
                    body = body.replace(i,"")
            elif "<span" in string:
                string = string.replace('\n', "")
                com = re.compile(r'<span.+?</span>')
                match = com.findall(string)
                for i in match:
                    body = string.replace(i, "")
                    body = body.replace('</a>', '')
                    com2 = re.compile('<a .+?>')
                    match = com2.findall(string)
                    for i in match:
                        body = body.replace(i,"")
            else:
                body = string

            # print title
            # print pub_date
            # print body
            # print url
            # print publisher
            cur.execute("insert into blogs_blogspost(title,pub_date,body,url,publisher) values('%s','%s','%s','%s','%s')" % (title,pub_date,body,url,publisher))

        except:
            pass
    print "rss源%s更新博客%d篇" % (url, len(lists))
    for i in lists:
        print i.title
    print "-----------------"

cur.execute("delete from blogs_blogspost  where id in (select id from (select  max(id) as id,count(url) as count from blogs_blogspost group by url having count >1 order by count desc) as tab )")
cur.close()
conn.commit()
conn.close()
