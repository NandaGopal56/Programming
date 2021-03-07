from bs4 import  BeautifulSoup
import requests


url="https://beebom.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content,'lxml')

'''
title = soup.title
print(title)

name = soup.title.name
print(name)

name = soup.name
print(name)'''
#getting the title of the website
name_string = soup.title.string
print(name_string)

#getting the titles of different articles
article_titles = []
title = soup.findAll('div',class_="td-module-thumb")
for t in title:
    article_titles.append(t.a["title"])

#getting the links of the articles
article_links = []
h3_tags = soup.findAll('h3',class_="entry-title td-module-title")

for h3 in h3_tags:
    article_links.append(h3.a["href"])

#looping through all the articles to to print the article-title,article-link and the content of the articles
for i in range(len(article_links)):
    #printing the title of the article
    print(article_titles[i])
    print("*********************************************************************************************************************************")
    #printing the link to the specific article
    print(article_links[i])
    print("*********************************************************************************************************************************")
    #visiting all the article links in the article_links list
    page = requests.get(article_links[i])

    #making soup object for all the article
    soup = BeautifulSoup(page.content,"lxml")

    #finding the p-tag of the articles page
    p_tag = soup.findAll('p')

    for p in p_tag:
        #getting the text content of the article page
        print(p.text)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print()


