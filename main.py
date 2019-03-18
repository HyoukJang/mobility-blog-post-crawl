from numpy import *
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from selenium import webdriver
import uber
import lyft
from rake_nltk import Rake



def extractKeywords(text_list):
    r = Rake()
    keywords_list = []

    for text in text_list:
        r.extract_keywords_from_text(text)
        extract = r.get_ranked_phrases_with_scores()
        if len(extract) >= 2:
            keywords_list.append(extract[0][1] + ", " + extract[1][1])
        else:
            keywords_list.append(extract[0][1])

        # print(extract[0][1]+ ", "+ extract[1][1])
        # print(" ")

    return keywords_list


def describeMyWords(title, excerpt, title_keywords, excerpt_keywords):

    my_keywords_list = [None] * len(title_keywords)

    for idx, total_keywords in enumerate(zip(title, excerpt, title_keywords, excerpt_keywords)):

        txt = total_keywords[0] + total_keywords[1] + total_keywords[2] + total_keywords[3]
        # print(txt)
        # print(type(txt))

        if "GPS" in txt:
            my_keywords_list[idx] = "GPS improvement "

        if "Mapbox" in txt:
            my_keywords_list[idx] = "Map"

        if "map" in txt:
            my_keywords_list[idx] = "Map"

        if "visualization" in txt:
            my_keywords_list[idx] = "Visualization"

        if "kepler.gl" in txt:
            my_keywords_list[idx] = "Visualization"


    return my_keywords_list




options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('./chromedriver', options=options)

header = ['company', 'category', 'title', 'subtitle', 'link', 'year', 'month', 'day', 'excerpt']

uber_result = uber.uberCrawl(driver)
lyft_result = lyft.lyftCrawl(driver)

uber_result_dataframe = pd.DataFrame(uber_result, columns= header)
lyft_result_dataframe = pd.DataFrame(lyft_result, columns= header)

result_dataframe = uber_result_dataframe.append(lyft_result_dataframe)

# print(result_dataframe.shape)

#temp = result_dataframe.sort_values(by=['title'], axis=0)
temp = result_dataframe.drop_duplicates(['title'], keep='first')
temp = temp.replace('engineering', 'general-engineering')
temp = temp.replace('uberdata', 'data')
temp = temp.replace('data-science', 'data')
temp = temp.replace('open-source-articles', 'open-source')

temp['keywords_title'] = extractKeywords(temp['title'].tolist())
temp['keywords_excerpt'] = extractKeywords(temp['excerpt'].tolist())
temp['myKeywords'] = describeMyWords(temp['title'].tolist(), temp['excerpt'].tolist(), temp['keywords_title'].tolist(), temp['keywords_excerpt'].tolist())

# print(temp['myKeywords'])



# print(temp['company'].value_counts())
# print(temp['category'].value_counts())
# print(temp['year'].value_counts())



temp.to_csv('total_mobility_engineering_blog_posts.csv', index=False)

# uber_result_dataframe['title_ko'] = translate(uber_result_dataframe['title'].tolist())
# uber_result_dataframe['subtitle_ko'] = translate(uber_result_dataframe['subtitle'].tolist())
# uber_result_dataframe['excerpt_ko'] = translate(uber_result_dataframe['excerpt'].tolist())

# print(uber_result_dataframe.head())

