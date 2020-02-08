from selenium import webdriver
import re
import urllib.request
import requests
def chunk_download(IMAGE_URL,i):
    urllib.request.urlretrieve(IMAGE_URL[0], filename='./'+str(i)+'.png')



if __name__ == '__main__':
    with open('website.txt', 'r', encoding='utf-8') as file:
        file.readline()
        i=1
        for url in file:
            """Method  1"""
            driver = webdriver.PhantomJS(
                # 对应的phantomjs包的地址
                executable_path=r'/Users/name/phantomjs-2.1.1-macosx/bin/phantomjs')
            driver.get(url)
            source = driver.page_source
            """ """
            """Method  2"""
            # source = requests.get(url)
            # source.encoding = 'utf-8'
            # source = source.text
            # print(source)
            """ """
            # 正则匹配
            res_peper = r'var msg_cdn_url = "(.*?)";'
            m_peper = re.findall(res_peper, source, re.S | re.M)
            # print(m_peper)
            chunk_download(m_peper,i)
            i=i+1
