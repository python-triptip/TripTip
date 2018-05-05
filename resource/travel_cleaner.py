import csv

with open('travel_raw.csv', newline='') as f:
    reader = csv.reader(f)
    with open('travel_cleaned.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(["City Name", "Tour Name", "Price", "Rating", "Review Number", "Web Link"])

        count = 0
        for row in reader:
            if count == 0:
                count += 1
                continue
            city = row[0]
            name = row[1].rstrip("...")
            price = row[2][1:-1]
            price.lstrip("$").rstrip("*")

            rating = row[3][-2:]
            print(rating)
            try:
                rating = float(rating) / 10
            except:
                rating = ""
            review = row[4][:-8]
            url = row[5]
            if len(url) > 5:
                url = "https://www.tripadvisor.com" + url
            spamwriter.writerow([city, name, price, rating, review, url])
            count += 1
