from bs4 import BeautifulSoup
from dateutil.parser import parse


def replace(str):
    str = str.replace("’", "\'")
    str = str.replace("…", ".")
    str = str.replace("“", "\"")
    str = str.replace("”", "\"")

    return str



def lyftCrawl(driver):

    lyft_source_url = "https://eng.lyft.com/tagged/"
    lyft_query = ['data', 'data-science', 'engineering', 'mobile', 'product', 'security']
    lyft_url_list = [lyft_source_url + query for query in lyft_query]

    lyft_result=[]
    # f = open('lyft_post_list.csv', 'w', encoding='utf-8', newline='')
    # wr = csv.writer(f)
    # wr.writerow(['category', 'title', 'subtitle', 'link','year','month', 'day','excerpt'])



    for lyft_url in lyft_url_list:

        driver.get(lyft_url)
        section = driver.page_source

        soup = BeautifulSoup(section, "html.parser")

        lyft_articlelist = soup.find_all('div', {
            'class': 'postArticle postArticle--short js-postArticle js-trackPostPresentation js-trackPostScrolls'})

        for article in lyft_articlelist:


            title = replace(article.find('h3', {
                'class': ['graf graf--h3 graf-after--figure graf--title', 'graf graf--h3 graf--leading graf--title',
                          'graf graf--h3 graf-after--figure graf--trailing graf--title',
                          'graf graf--h3 graf--hasDropCapModel graf--leading graf--title']}).text).strip()
            subtitle = article.find('h4', {'class': ['graf graf--h4 graf-after--h3 graf--subtitle','graf graf--h4 graf-after--h3 graf--trailing graf--subtitle']})

            if subtitle is not None:
                subtitle = replace(subtitle.text)
            else:
                subtitle = "No subtitle"

            category = lyft_query[lyft_url_list.index(lyft_url)]

            href = article.find('a', {'class': 'button button--smaller button--chromeless u-baseColor--buttonNormal'})[
                'href']

            time = article.find('time').text

            year, month, day = parse(time).year, parse(time).month, parse(time).day

            excerpt = article.find('p', {
                'class': ['graf graf--p graf-after--h3 graf--trailing', 'graf graf--p graf-after--h3',
                          'graf graf--p graf-after--h4 graf--trailing']})
            if excerpt is not None:
                excerpt = replace(excerpt.text)
            else:
                excerpt = "No excerpt"

            # print(category)
            # print(title)
            # print(subtitle)
            # print(href)
            # print(year)
            # print(month)
            # print(day)
            # print(excerpt)
            # print(" ")

            lyft_result.append(['lyft', category, title, subtitle, href, year, month, day, excerpt])

    return lyft_result
# f.close()

