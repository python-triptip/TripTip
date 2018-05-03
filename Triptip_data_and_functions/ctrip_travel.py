import os
import sys
import bs4
import translate_test
from bs4 import BeautifulSoup as bs
import urllib, urllib.request, csv

# instructions
# https://docs.google.com/document/d/1IC-Ytwkzj22CAf5-ppNMAUB4ZdMhLEG71ySg3-Sm92E/edit?usp=sharing


websites = ["http://you.ctrip.com/sight/beijing1.html",
            "http://you.ctrip.com/sight/shanghai2.html",
            "http://you.ctrip.com/sight/guangzhou152.html",
            "http://you.ctrip.com/sight/hangzhou14.html",
            "http://you.ctrip.com/sight/sanya61.html",
            "http://you.ctrip.com/sight/chengdu104.html",
            "http://you.ctrip.com/sight/xiamen21.html",
            "http://you.ctrip.com/sight/guilin28.html",
            "http://you.ctrip.com/sight/lhasa36.html",
            "http://you.ctrip.com/sight/yili115.html",
            "http://you.ctrip.com/sight/qingdao5.html",
            "http://you.ctrip.com/sight/jinan128.html",
            "http://you.ctrip.com/sight/chongqing158.html",
            "http://you.ctrip.com/sight/aba744.html",
            "http://you.ctrip.com/sight/hongkong38.html",
            "http://you.ctrip.com/sight/taipeicity360.html",
            "http://you.ctrip.com/sight/gaoxiong756.html",
            "http://you.ctrip.com/sight/macau39.html",
            "http://you.ctrip.com/sight/hulunbeier458.html",
            "http://you.ctrip.com/sight/chifeng483.html",
            "http://you.ctrip.com/sight/leshan103.html",
            "http://you.ctrip.com/sight/qianxinan1428.html",
            "http://you.ctrip.com/sight/haixi120012.html",
            "http://you.ctrip.com/sight/haerbin151.html",
            "http://you.ctrip.com/sight/kualalumpur45.html",
            "http://you.ctrip.com/sight/kyoto430.html",
            "http://you.ctrip.com/sight/okinawa292.html",
            "http://you.ctrip.com/sight/singapore53.html"
            ]

cityName = ["Beijing", "Shanghai", "Guangzhou", "Hangzhou", "Sanya", "Chengdu", "Xiamen", "Guilin", "Lhasa", "Ili",
            "Qingdao", "Jinan", "Chongqing", "Aba", "Hong Kong", "Taipei", "Gaoxiong", "Macau", "Hulunbeier", "Chifeng",
            "Leshan", "Qianxinan", "Haixi", "Harbin", "Kuala Lumpur", "Kyoto", "Okinawa", "Singapore"]

with open('ctrip_travel.csv', 'w', newline='') as csvfile:
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
                    review = rating_review.select("a.recomment")[0].text.strip()
            print(rating)
            print(review)

            spamwriter.writerow([cityName[i], name, price, rating, review, url])
