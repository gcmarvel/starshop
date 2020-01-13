import datetime
from datetime import timedelta
import random
import csv
import os


with open('catalogue_data.csv', 'r') as data:
    with open('catalogue_data_new.csv', 'w') as data_new:
        data_reader = csv.DictReader(data)
        data_writer = csv.DictWriter(data_new, fieldnames=['starid', 'name', 'country', 'magnitude', 'constellation', 'date'])

        data_writer.writeheader()

        c = 0
        working_date = datetime.date(1999, 2, 11)

        for line in data_reader:
            if c < 7140:
                while True:
                    x = random.randint(1, 3)
                    c += 1
                    working_date += timedelta(1)
                    if x == 3:
                        if line['date'] == '':
                            data_writer.writerow({'starid': line['starid'], 'name': line['name'], 'country': line['country'], 'magnitude': line['magnitude'], 'constellation': line['constellation'], 'date': working_date})
                        else:
                            data_writer.writerow({'starid': line['starid'], 'name': line['name'], 'country': line['country'], 'magnitude': line['magnitude'], 'constellation': line['constellation'], 'date': line['date']})
                            working_date = datetime.datetime.strptime(line['date'], '%Y-%m-%d')
                        break

            if 7140 <= c < 8165:
                while True:
                    c += 1
                    x = random.randint(1, 3)
                    if x == 3:
                        working_date += timedelta(1)
                    if line['date'] == '':
                        data_writer.writerow({'starid': line['starid'], 'name': line['name'], 'country': line['country'], 'magnitude': line['magnitude'], 'constellation': line['constellation'], 'date': working_date})
                    else:
                        data_writer.writerow({'starid': line['starid'], 'name': line['name'], 'country': line['country'], 'magnitude': line['magnitude'], 'constellation': line['constellation'], 'date': line['date']})
                        working_date = datetime.datetime.strptime(line['date'], '%Y-%m-%d')
                    break

            if 8165 <= c:
                while True:
                    c += 1
                    x = random.randint(1, 5)
                    if x == 3:
                        working_date += timedelta(1)
                    if line['date'] == '':
                        data_writer.writerow({'starid': line['starid'], 'name': line['name'], 'country': line['country'], 'magnitude': line['magnitude'], 'constellation': line['constellation'], 'date': working_date})
                    else:
                        data_writer.writerow({'starid': line['starid'], 'name': line['name'], 'country': line['country'], 'magnitude': line['magnitude'], 'constellation': line['constellation'], 'date': line['date']})
                        working_date = datetime.datetime.strptime(line['date'], '%Y-%m-%d')
                    break

os.remove('catalogue_data.csv')
os.rename('catalogue_data_new.csv', 'catalogue_data.csv')


with open('reviews.csv', 'r') as raw:
    with open('reviewsdate.csv', 'w') as final:

        reader = csv.DictReader(raw)
        writer = csv.DictWriter(final, fieldnames=['review', 'name', 'date', 'image'])

        writer.writeheader()

        working_date = datetime.date(2009, 2, 11)

        for line in reader:

            if working_date.year < 2010:
                working_date += timedelta(random.randint(90, 240))

            elif working_date.year < 2016:
                working_date += timedelta(random.randint(60, 120))

            elif working_date.year < 2019:
                working_date += timedelta(random.randint(30, 60))

            elif working_date.year >= 2019:
                working_date += timedelta(random.randint(6, 14))

            if line['date'] == '':
                writer.writerow({'review': line['review'], 'name': line['name'], 'date': working_date, 'image': line['image']})

            else:
                writer.writerow({'review': line['review'], 'name': line['name'], 'date': line['date'], 'image': line['image']})
                working_date = datetime.datetime.strptime(line['date'], '%Y-%m-%d')

os.remove('reviews.csv')
os.rename('reviewsdate.csv', 'reviews.csv')

with open('reviews.csv', 'r') as raw:
    with open('reviewsdate.csv', 'w') as final:

        reader = csv.DictReader(raw)
        writer = csv.DictWriter(final, fieldnames=['review', 'name', 'date', 'image'])

        writer.writeheader()

        image_list = ["static/img/sm-detail/sm-blue1.png", "static/img/sm-detail/sm-blue2.png", "static/img/sm-detail/sm-blue3.png", "static/img/sm-detail/sm-blue4.png",
                      "static/img/sm-detail/sm-double1.png", "static/img/sm-detail/sm-double2.png", "static/img/sm-detail/sm-double3.png", "static/img/sm-detail/sm-double4.png",
                      "static/img/sm-detail/sm-orange1.png", "static/img/sm-detail/sm-orange2.png", "static/img/sm-detail/sm-orange3.png", "static/img/sm-detail/sm-orange4.png",
                      "static/img/sm-detail/sm-red1.png", "static/img/sm-detail/sm-red2.png", "static/img/sm-detail/sm-red3.png", "static/img/sm-detail/sm-red4.png",
                      "static/img/sm-detail/sm-white1.png", "static/img/sm-detail/sm-white2.png", "static/img/sm-detail/sm-white3.png", "static/img/sm-detail/sm-white4.png",
                      "static/img/sm-detail/sm-yellow1.png", "static/img/sm-detail/sm-yellow2.png", "static/img/sm-detail/sm-yellow3.png", "static/img/sm-detail/sm-yellow4.png",]

        for line in reader:

            if line['image'] == '':
                writer.writerow({'review': line['review'], 'name': line['name'], 'date': line['date'], 'image': random.choice(image_list)})

            else:
                writer.writerow({'review': line['review'], 'name': line['name'], 'date': line['date'], 'image': line['image']})
                working_date = datetime.datetime.strptime(line['date'], '%Y-%m-%d')

os.remove('reviews.csv')
os.rename('reviewsdate.csv', 'reviews.csv')


