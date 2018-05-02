import os
import sys
import bs4
from bs4 import BeautifulSoup as bs
import urllib, urllib.request, csv

# instructions
# https://docs.google.com/document/d/1IC-Ytwkzj22CAf5-ppNMAUB4ZdMhLEG71ySg3-Sm92E/edit?usp=sharing

websites = ["https://www.tripadvisor.com/Restaurants-g294212-Beijing.html",
            "https://www.tripadvisor.com/Restaurants-g308272-Shanghai.html",
            "https://www.tripadvisor.com/Restaurants-g298555-Guangzhou_Guangdong.html",
            "https://www.tripadvisor.com/Restaurants-g298559-Hangzhou_Zhejiang.html",
            "https://www.tripadvisor.com/Restaurants-g298184-Tokyo_Tokyo_Prefecture_Kanto.html",
            "https://www.tripadvisor.com/Restaurants-g298564-Kyoto_Kyoto_Prefecture_Kinki.html",
            "https://www.tripadvisor.com/Restaurants-g298566-Osaka_Osaka_Prefecture_Kinki.html",
            "https://www.tripadvisor.com/Restaurants-g293916-Bangkok.html",
            "https://www.tripadvisor.com/Restaurants-g293917-Chiang_Mai.html",
            "https://www.tripadvisor.com/Restaurants-g294197-Seoul.html",
            "https://www.tripadvisor.com/Restaurants-g297884-Busan.html",
            "https://www.tripadvisor.com/Restaurants-g304554-Mumbai_Maharashtra.html",
            "https://www.tripadvisor.com/Restaurants-g297628-Bengaluru_Bangalore_District_Karnataka.html",
            "https://www.tripadvisor.com/Restaurants-g304551-New_Delhi_National_Capital_Territory_of_Delhi.html",
            "https://www.tripadvisor.com/Restaurants-g294265-Singapore.html",
            "https://www.tripadvisor.com/Restaurants-g298570-Kuala_Lumpur_Wilayah_Persekutuan.html",
            "https://www.tripadvisor.com/Restaurants-g293890-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html",
            "https://www.tripadvisor.com/Restaurants-g293962-Colombo_Western_Province.html",
            "https://www.tripadvisor.com/Restaurants-g293925-Ho_Chi_Minh_City.html",
            "https://www.tripadvisor.com/Restaurants-g293924-Hanoi.html"]

cityName = ["Beijing", "Shanghai", "Guangzhou", "Hangzhou", "Tokyo", "Kyoto", "Osaka", "Bangkok", "Chiang Mai",
            "Seoul", "Busan", "Mumbai", "Bengaluru", "New Delhi", "Singapore", "Kuala", "Kathmandu", "Colombo",
            "Ho Chi Minh City", "Hanoi"]

with open('restaurant.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["City Name", "Restaurant Name", "Price", "Rating", "Review Number", "Web Link"])

    for i in range(len(websites)):
        page = urllib.request.urlopen(websites[i])
        soup = bs(page, "html.parser")
        body = soup.body
        products = body.select("div.detail")
        for product in products:
            name = ""
            url = ""
            nameList = product.select("div.item.name > a")
            if len(nameList) > 0:
                name = nameList[0].text
                url = nameList[0].get("href")
            print(name)
            print(url)

            price = ""
            priceList = product.select("div.item.price")
            if len(priceList) > 0:
                price = priceList[0].text
            print(price)

            rating = ""
            review = ""
            rating_reviewList = product.select("div.item.rating-count")
            if len(rating_reviewList) > 0:
                rating = rating_reviewList[0].select("div.rating-widget > div > span")[0].get("class")[1]
                review = rating_reviewList[0].select("a.review_count")[0].text
            print(review)
            print(rating)

            spamwriter.writerow([cityName[i], name, price, rating, review, url])




