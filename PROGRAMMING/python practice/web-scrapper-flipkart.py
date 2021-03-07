import requests
import bs4

url = "https://www.flipkart.com/realme-c3-frozen-blue-32-gb/p/itm58bf81a807d66?pid=MOBFZHC5HAGKGBBW&lid=LSTMOBFZHC5HAGKGBBWJH2HLH&marketplace=FLIPKART&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=ee5faf66-61a9-4ade-a95a-3968fcd6138a.MOBFZHC5HAGKGBBW.SEARCH&ppt=sp&ppn=sp&ssid=hfuw86qsrk0000001588701374218&qH=eb4af0bf07c16429"

page = requests.get(url)

#making the soup object
soup = bs4.BeautifulSoup(page.content,'lxml')

#getting the title of the page
print(soup.title.string)

#getting the product title
product_title = soup.find('span',class_="_35KyD6")
print(product_title.text)

#getting the product price
product_price = soup.find('div',class_="_1vC4OE _3qQ9m1")
print("price is: ",product_price.text)