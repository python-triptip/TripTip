import csv

with open('restaurant_cleaned.csv', newline='') as f1:
    restaurant_reader = csv.reader(f1)
    with open('travel_cleaned.csv', newline='') as f2:
        travel_reader = csv.reader(f2)

        with open('data_merge.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(["City Name", "Type", "Name", "Price", "Price Level", "Rating", "Review Number", "Web Link"])

            count = 0
            for row in travel_reader:
                if count == 0:
                    count += 1
                    continue
                city = row[0]
                name = row[1]
                price = row[2]
                rating = row[3]
                print(rating)
                review = row[4]
                url = row[5]
                spamwriter.writerow([city, "Tourism", name, price, "", rating, review, url])

            count = 0
            for row in restaurant_reader:
                if count == 0:
                    count += 1
                    continue
                city = row[0]
                name = row[1]
                price = row[2]
                rating = row[3]
                print(rating)
                review = row[4]
                url = row[5]
                spamwriter.writerow([city, "Restaurant", name, "", price, rating, review, url])
