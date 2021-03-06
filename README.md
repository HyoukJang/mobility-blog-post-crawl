# Mobility-Engineering-blog-post-crawl
To collect engineering blog posts infos (NOT whole post contents) of leading mobility companies such as Uber, Lyft

## Engineering Blog Lists

- Uber Engineering Blog
    - https://eng.uber.com
    - AI, Architecture, Culture, General-Engineering, Mobile, Open Source, Uber Data

- Lyft Engineering Blog
    - https://eng.lyft.com
    - Data, Data Science, Engineering, Mobile, Product, Security
 
    In this project, I merged several categories between Uber and Lyft contents becasuse of readability as below.
    - General-Engineering - Engineering
    - Uber Data - Data - Data Science
    - Open source articles - open source



## Requirements

To crawl blog post info(Title, Excerpt, etc), use Selenium and Chromedriver.
Chromedriver(for OS X) is included. If you use Windows, Linux, etc, please include the concrete chromedriver file in the root directory.  

**Notice! Chromedriver ver. is 75.0.3770.90. Please check chrome version which you have before run** 

Basic data science libraries and rake-nltk to extract keywords.

```
pip install selenium
pip install rake-nltk
pip install bs4
pip install dateutil
pip install pandas
pip install numpy
```


## How to use

1. Run main.py
2. 'total_mobility_engineering_blog_posts.csv' will be created in same directory with main.py

## CSV Headers Info

- company
- category
- title
- subtitle
- link
- year
- month
- day
- excerpt
- keywords_title
- keywords_excerpt
- myKeywords


