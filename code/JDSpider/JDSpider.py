import requests
import json 
import time
from pyquery import  PyQuery as pq 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
keyWord = 'ipad'

def getPage(page):

    print('爬取第'+str(page)+'页的商品')
    try:
        url='https://search.jd.com/Search?keyword='+quote(keyWord)
        browser.get(url)
        if page>1:
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'.p-skip .input-txt'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'.p-skip .btn'))
            )
            input.clear()
            #print(input)
            #print(str(page))
            input.send_keys(str(page))
            #time.sleep(100)
            #js2 = 'var q=document.querySelector('.p-skip').children[3].click()'
            browser.execute_script("var q=document.querySelector('.p-skip').children[3].click()")
            #submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.p-wrap .curr'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.gl-warp')))
        parsePage()
    except TimeoutException as e:
        print('第'+str(page)+'页超时')
        getPage(page)
        


def parsePage():

    html = browser.page_source
    doc = pq(html)
    items = doc('#J_goodsList .gl-warp .gl-item').items()
    for item in items:
        product = {
            #图片懒加载,还未能获取
            'image':item.find('.p-img a img').attr('src'),
            'url':item.find('.p-img a').attr('href')
            'price':item.find('.p-price').text(),
            'detaile':item.find('.p-name').text(),
            'shop':item.find('.p-shop').text(),
            'commit':item.find('.p-commit').text()
        }
        print(product)
        saveItems(product)

def saveItems(item):
    with open('Jd.json','a',encoding='utf-8') as file:
        file.write(json.dumps(item,indent=2,ensure_ascii=False))
        file.write('\n')   

def test():
        url='https://search.jd.com/Search?keyword='+quote(keyWord)
        browser.get(url)
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.gl-warp')))
        input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'.p-skip .input-txt'))
            )
        input.clear()
        time.sleep(10)
        input.send_keys("2")

def main():
    for i in range(1,100):
        getPage(i)
        #tiem.sleep(1)
    
    #browser.close()

if __name__ == "__main__":
    main()
    #test()

