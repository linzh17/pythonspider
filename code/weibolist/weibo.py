import requests
import json
from urllib.parse import urlencode
from pyquery import PyQuery as pq


baseUrl = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?'

headers =  {
    'Host':'www.zhihu.com',
    'Referer':'https://www.zhihu.com/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Requested-With':'fetch',
    'cookie':'_zap=bfd22326-b760-4a38-af8d-5e4b966ef33d; d_c0="AMBlBTOpKA6PTpJCN264C8SN83faeNivSL8=|1536026877"; z_c0=Mi4xY2ZsOEJBQUFBQUFBd0dVRk02a29EaGNBQUFCaEFsVk4tWWs2WFFDbm8tZXVmcEFVVXU5enUtWjZkM1ZLNFUtdWNB|1548565497|f3872984f62e4753236db0b385097cdd00603e99; q_c1=75c01ebad41f4963a0ff0fed77bc32f2|1551015694000|1536026879000; _xsrf=e0ed09b9068f31e631d2df496e8338e4; __utmz=51854390.1551015705.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20170323=1^3=entry_date=20170323=1; _xsrf=ycT68JLKffj7mQd23pwu4lq7jppFUqBz; __utma=51854390.1970861218.1551015705.1551015705.1551018354.2; tst=r; tgw_l7_route=060f637cd101836814f6c53316f73463'}


params = {
        'session_token':'f71d383a824cc66d0c0be329ba648f47',
        'desktop':'true',
        'page_number':3,
        'limit':'6',
        'action':'down',
        'after_id':11,
    }
url = baseUrl+urlencode(params)

def getPage(url):
    print(url)

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('error')

#print(getPage(1)['paging']['next'])

def parse_page(json):
    if json:
        items = json.get('data')
        for item in items:
            item=item.get('target')
            zhihu={}
            zhihu['name']=item.get('author')['name']
            zhihu['question']=item.get('question',{'title':'None'})['title']
            zhihu['answer']=pq(item.get('content')).text()
            zhihu['comments']=item.get('comment_count')
            zhihu['created_time']=item.get('created_time')
            yield zhihu 

def writeToFile(content):
    with open('zhihuList.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


for i in range(1,1000):
    jsonget = getPage(url)
    url = jsonget['paging']['next']
    results = parse_page(jsonget)
    for result in results:
        print(result)
        writeToFile(result) 

    print('='*50)