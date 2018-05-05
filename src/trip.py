import csv
import heapq as hq

class TripInfo:

    def __init__(self, info, type):
        self.city = info[0]
        self.name = info[1]
        self.price = info[2]
        self.rating = info[3]
        self.review = info[4]
        self.link = info[5]
        self.type = type

    def __lt__(self, other):
        return self.review < other.review

trip_db = []

with open('ctrip_restaurant_cleaned.csv', newline='') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if count == 0:
            count += 1
            continue
        info = TripInfo(row, "Restaurant")
        trip_db.append(info)
    # print(count)

with open('ctrip_travel_cleaned.csv', newline='') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if count == 0:
            count += 1
            continue
        info = TripInfo(row, "Tourism")
        trip_db.append(info)
    # print(count)

with open('restaurant_cleaned.csv', newline='') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if count == 0:
            count += 1
            continue
        prices = row[2].split(" - ")
        total = 0
        for price in prices:
            total += price.count('$') * 25
        if len(prices) != 0:
            total = total * 1.0 / len(prices)
        row[2] = str(total)
        info = TripInfo(row, "Restaurant")
        trip_db.append(info)
        # print(row[1], row[2] ,prices)

    # print(count)

with open('travel_cleaned.csv', newline='') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if count == 0:
            count += 1
            continue
        info = TripInfo(row, "Tourism")
        trip_db.append(info)
    # print(count)


# for ele in trip_db:
#     print(ele.name)
# print(len(trip_db))

def tourism_based_on_budget(city, budget):
    cityInfo = []
    for info in trip_db:
        if info.city.lower().strip() == city.lower().strip() and info.type == "Tourism":
            review = 0
            try:
                review = int(info.review)
            except:
                continue
            hq.heappush(cityInfo, (-review, info))

    money = float(budget)
    outputInfo = []
    duplicate_set = {""}
    while len(cityInfo) > 0:
        info = hq.heappop(cityInfo)[1]
        price = 0
        try:
            price = float(info.price)
        except:
            price = 0
        if money - price < 0:
            continue
        if info.name not in duplicate_set:
            outputInfo.append(info)
            duplicate_set.add(info.name)
    return outputInfo

def restaurant_based_on_budget(city, budget):
    cityInfo = []
    for info in trip_db:
        if info.city.lower().strip() == city.lower().strip() and info.type == "Restaurant":
            review = 0
            try:
                review = int(info.review)
            except:
                continue
            hq.heappush(cityInfo, (-review, info))

    money = float(budget)
    outputInfo = []
    duplicate_set = {""}
    while len(cityInfo) > 0:
        info = hq.heappop(cityInfo)[1]
        price = 0
        try:
            price = float(info.price)
        except:
            price = 0
        if money - price < 0:
            continue
        if info.name not in duplicate_set:
            outputInfo.append(info)
            duplicate_set.add(info.name)
    return outputInfo