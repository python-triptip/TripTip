import os
import sys
import bs4
from bs4 import BeautifulSoup as bs
import urllib, urllib.request, csv

# instructions
# https://docs.google.com/document/d/1IC-Ytwkzj22CAf5-ppNMAUB4ZdMhLEG71ySg3-Sm92E/edit?usp=sharing


websites = ["http://you.ctrip.com/restaurantlist/beijing1.html",
            "http://you.ctrip.com/restaurantlist/shanghai2.html",
            "http://you.ctrip.com/restaurantlist/guangzhou152.html",
            "http://you.ctrip.com/restaurantlist/hangzhou14.html",
            "http://you.ctrip.com/restaurantlist/sanya61.html",
            "http://you.ctrip.com/restaurantlist/chengdu104.html",
            "http://you.ctrip.com/restaurantlist/xiamen21.html",
            "http://you.ctrip.com/restaurantlist/guilin28.html",
            "http://you.ctrip.com/restaurantlist/lhasa36.html",
            "http://you.ctrip.com/restaurantlist/yili115.html",
            "http://you.ctrip.com/restaurantlist/qingdao5.html",
            "http://you.ctrip.com/restaurantlist/jinan128.html",
            "http://you.ctrip.com/restaurantlist/chongqing158.html",
            "http://you.ctrip.com/restaurantlist/aba744.html",
            "http://you.ctrip.com/restaurantlist/hongkong38.html",
            "http://you.ctrip.com/restaurantlist/taipeicity360.html",
            "http://you.ctrip.com/restaurantlist/gaoxiong756.html",
            "http://you.ctrip.com/restaurantlist/macau39.html",
            "http://you.ctrip.com/restaurantlist/hulunbeier458.html",
            "http://you.ctrip.com/restaurantlist/chifeng483.html",
            "http://you.ctrip.com/restaurantlist/leshan103.html",
            "http://you.ctrip.com/restaurantlist/qianxinan1428.html",
            "http://you.ctrip.com/restaurantlist/haixi120012.html",
            "http://you.ctrip.com/restaurantlist/haerbin151.html",
            "http://you.ctrip.com/restaurantlist/kualalumpur45.html",
            "http://you.ctrip.com/restaurantlist/kyoto430.html",
            "http://you.ctrip.com/restaurantlist/okinawa292.html",
            "http://you.ctrip.com/restaurantlist/singapore53.html"
            ]

cityName = ["Beijing", "Shanghai", "Guangzhou", "Hangzhou", "Sanya", "Chengdu", "Xiamen", "Guilin", "Lhasa", "Ili",
            "Qingdao", "Jinan", "Chongqing", "Aba", "Hong Kong", "Taipei", "Gaoxiong", "Macau", "Hulunbeier", "Chifeng",
            "Leshan", "Qianxinan", "Haixi", "Harbin", "Kuala Lumpur", "Kyoto", "Okinawa", "Singapore"]

with open('ctrip_restaurant.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["City Name", "Tour Name", "Price", "Rating", "Review Number", "Web Link"])

    for i in range(len(websites)):
        page = urllib.request.urlopen(websites[i])
        soup = bs(page, "html.parser")
        body = soup.body
        products = body.select("div.rdetailbox")
        for product in products:
            name = ""
            url = ""
            nameList = product.select("dt > a")
            if len(nameList) > 0:
                name = nameList[0].text
                url = nameList[0].get("href")
            print(name)
            print(url)

            price = ""
            priceList = product.select("span.price")
            if len(priceList) > 0:
                price = priceList[0].text
            print(price)

            rating = ""
            review = ""
            rating_reviewList = product.select("ul.r_comment")
            if len(rating_reviewList) > 0:
                rating_review = rating_reviewList[0]
                rating = rating_review.select("a.score > strong")[0].text
                if len(rating_review.select("a.recomment")) > 0:
                    review = rating_review.select("a.recomment")[0].text
            print(rating)
            print(review)

            spamwriter.writerow([cityName[i], name, price, rating, review, url])