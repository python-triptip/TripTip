import os
import sys
import bs4
from bs4 import BeautifulSoup as bs
import urllib, urllib.request, csv

# instructions
# https://docs.google.com/document/d/1IC-Ytwkzj22CAf5-ppNMAUB4ZdMhLEG71ySg3-Sm92E/edit?usp=sharing


websites = ["https://www.tripadvisor.com/Attractions-g294212-Activities-Beijing.html",
            "https://www.tripadvisor.com/Attractions-g308272-Activities-Shanghai.html",
            "https://www.tripadvisor.com/Attractions-g298555-Activities-Guangzhou_Guangdong.html",
            "https://www.tripadvisor.com/Attractions-g298559-Activities-Hangzhou_Zhejiang.html",
            "https://www.tripadvisor.com/Attractions-g298184-Activities-Tokyo_Tokyo_Prefecture_Kanto.html",
            "https://www.tripadvisor.com/Attractions-g298564-Activities-Kyoto_Kyoto_Prefecture_Kinki.html",
            "https://www.tripadvisor.com/Attractions-g298566-Activities-Osaka_Osaka_Prefecture_Kinki.html",
            "https://www.tripadvisor.com/Attractions-g293916-Activities-Bangkok.html",
            "https://www.tripadvisor.com/Attractions-g293917-Activities-Chiang_Mai.html",
            "https://www.tripadvisor.com/Attractions-g294197-Activities-Seoul.html",
            "https://www.tripadvisor.com/Attractions-g297884-Activities-Busan.html",
            "https://www.tripadvisor.com/Attractions-g304554-Activities-Mumbai_Maharashtra.html",
            "https://www.tripadvisor.com/Attractions-g297628-Activities-Bengaluru_Bangalore_District_Karnataka.html",
            "https://www.tripadvisor.com/Attractions-g304551-Activities-New_Delhi_National_Capital_Territory_of_Delhi.html",
            "https://www.tripadvisor.com/Attractions-g294265-Activities-Singapore.html",
            "https://www.tripadvisor.com/Attractions-g298570-Activities-Kuala_Lumpur_Wilayah_Persekutuan.html",
            "https://www.tripadvisor.com/Attractions-g293890-Activities-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html",
            "https://www.tripadvisor.com/Attractions-g293962-Activities-Colombo_Western_Province.html",
            "https://www.tripadvisor.com/Attractions-g293925-Activities-Ho_Chi_Minh_City.html",
            "https://www.tripadvisor.com/Attractions-g293924-Activities-Hanoi.html"]

cityName = ["Beijing", "Shanghai", "Guangzhou", "Hangzhou", "Tokyo", "Kyoto", "Osaka", "Bangkok", "Chiang Mai",
            "Seoul", "Busan", "Mumbai", "Bengaluru", "New Delhi", "Singapore", "Kuala", "Kathmandu", "Colombo",
            "Ho Chi Minh City", "Hanoi"]

with open('travel.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["City Name", "Tour Name", "Price", "Rating", "Review Number", "Web Link"])

    for i in range(len(websites)):
        page = urllib.request.urlopen(websites[i])
        soup = bs(page, "html.parser")
        body = soup.body
        products = body.select("div.product_details")
        for product in products:
            name = ""
            url = ""
            nameList = product.select("div.name_container > div.product_name > a")
            if len(nameList) > 0:
                name = nameList[0].text
                url = nameList[0].get("href")
            print(name)
            print(url)

            price = ""
            priceList = product.select("div.price > div.from > span")
            if len(priceList) > 0:
                price = priceList[0].text
            print(price)

            rating = ""
            review = ""
            rating_reviewList = product.select("div.rating_container > div.rating_and_reviews")
            if len(rating_reviewList) > 0:
                rating_review = rating_reviewList[0]
                rating = rating_review.select("div.rating-widget > div > span")[0].get("class")[1]
                if len(rating_review.select("div.reviews")) > 0:
                    review = rating_review.select("div.reviews")[0].text
            print(rating)
            print(review)

            spamwriter.writerow([cityName[i], name, price, rating, review, url])
