from bs4 import BeautifulSoup
from dateutil.parser import parse
from selenium import webdriver
from numpy import *
import pandas as pd

def replace(str):
    
    str = str.replace("’", "\'")
    
    return str




def uberCrawl(driver):
    

    uber_source_url = "https://eng.uber.com/category/articles/"
    uber_query = ['ai', 'architecture', 'culture', 'general-engineering', 'mobile', 'open-source-articles', 'uberdata']
    uber_url_list = [uber_source_url + query + '/' for query in uber_query]

    uber_result = []

    # f = open('uber_post_list.csv', 'w', encoding='utf-8', newline='')
    # wr = csv.writer(f)
    # wr.writerow(['category', 'title', 'link', 'year','month','day', 'excerpt'])
    
    for uber_url in uber_url_list:
    
        driver.get(uber_url)
    
        section = driver.page_source
    
        soup = BeautifulSoup(section, "html.parser")
    
        articlelist = soup.find_all('div', {'class': 'td_module_10 td_module_wrap td-animation-stack'})
    
        for article in articlelist:
    
    
            temp_for_title = article.find('h3', {'class': 'entry-title td-module-title'})
            temp_for_time = article.find('time', {'class': 'entry-date updated td-module-date'})
            temp_for_excerpt = article.find('div', {'class': 'td-excerpt'})
    
            category = uber_query[uber_url_list.index(uber_url)]
    
            title = replace(temp_for_title.find('a')['title']).strip()
            href = temp_for_title.find('a')['href']
            time = temp_for_time.text
            excerpt = replace(temp_for_excerpt.text.strip())
    
            year = parse(time).year
            month = parse(time).month
            day = parse(time).day
            
            # print(category)
            # print(title)
            # print(href)
            # print(year)
            # print(month)
            # print(day)
            # print(excerpt)
            # print(" ")
    
            uber_result.append(['uber', category, title, 'No subtitle', href, year, month, day, excerpt])

    
    return uber_result

# print(uber_total_posts_num)
# f.close

# 
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# 
# driver = webdriver.Chrome('/Users/hyoukjang/Downloads/chromedriver', options=options)
# uberCrawl(driver)

