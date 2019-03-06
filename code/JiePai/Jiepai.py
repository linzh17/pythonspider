import requests
import os
import time
from hashlib import md5
from urllib.parse import urlencode

headers ={
    'Host':'www.toutiao.com',
    'Referer':'https://www.toutiao.com/ch/gallery_old_picture/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'Cookie':'tt_webid=6663323848248755725; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1693831df34472-0f937e1740d2eb-162a1c0b-1fa400-1693831df35fe9; CNZZDATA1259612802=630908265-1551425067-https%253A%252F%252Fwww.google.com.hk%252F%7C1551425067; __tasessionId=5vwu7psj91551425986390; tt_webid=6663323848248755725; csrftoken=8e3462b8d4014dd38ca1b00b3c81c3da'
}

baseurl = 'https://www.toutiao.com/api/pc/feed/?'



def getPage(mbt):
    params = {
    'category':'gallery_old_picture',
    'utm_source':'toutiao',
    'max_behot_time':mbt,
    'as':'A1D5BC4788EE370',
    'cp':'5C78EEC347F0DE1',
    '_signature':'ErV2FQAATtIQGGHTC3py6xK1dg'
    }
    url = baseurl + urlencode(params)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('error')

def parsePage(json):
    if json:
        items = json.get('data')
        for item in items:
            title = item.get('title')
            image_list = item.get('image_list')
            for image in image_list:
                yield{
                    'image':image.get('url'),
                    'title':title
                }
        
def saveImage(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get('https:'+item.get('image'))
        if response.status_code == 200:
            file_path ='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)


def main(mbt):
    for i in range(1,3):
        jsonget = getPage(mbt)
        print(jsonget)
        for item in parsePage(jsonget):
            print(item)
            saveImage(item)
        mbt = jsonget.get('next')['max_behot_time']
        time.sleep(1)

if __name__ == '__main__':
    main(0)