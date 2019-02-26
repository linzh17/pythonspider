#example 1
import requests 
from  pyquery import PyQuery as pq

proxies = {
    'http':'socks5://127.0.0.1:1080',
    'https':'socks5://127.0.0.1:1080'
}

url  = 'https://www.zhihu.com/explore' 
headers = {
    
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
html = requests.get(url,headers=headers,proxies=proxies).text
doc = pq(html)  

items = doc('.explore-tab .explore-feed ').items()
print(items)
for item in items:
    print(item)
    question = item.find('h2').text()
    author = item.find('.author-link').text()
    answer = pq(item.find('.content').html()).text()
    # 参数a表示以追加的形式写入文件
    file = open('zhihu-explore.txt','a',encoding='utf-8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n' + '=' * 50 + '\n')
    #关闭文件对象
    file.close()