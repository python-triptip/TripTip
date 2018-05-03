import csv
import translate_test

with open('ctrip_restaurant_raw.csv', newline='') as f:
    reader = csv.reader(f)
    with open('ctrip_restaurant_cleaned2.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(["City Name", "Tour Name", "Price ($)", "Rating", "Review Number", "Web Link"])

        count = 0
        for row in reader:
            if count == 0:
                count += 1
                continue
            city = row[0]
            name = row[1]
            print(name)
            name = translate_test.translate(name)
            print(name)
            price = ""
            try:
                price = round(float(row[2][1:]) * 0.16, 2)
            except:
                price = ""

            rating = row[3]
            review = row[4][1:].rstrip(u"条点评)")

            url = row[5]
            if len(url) > 5:
                url = "http://you.ctrip.com" + url
            spamwriter.writerow([city, name, price, rating, review, url])
            count += 1
