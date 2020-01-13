import datetime
from datetime import timedelta
import csv


with open('catalogue_data.csv', 'r') as cat_data:
    data_reader = csv.DictReader(cat_data)
    data = []
    for line in data_reader:
        data.append({'starid': line['starid'], 'name': line['name'], 'country': line['country'], 'magnitude': line['magnitude'], 'constellation': line['constellation'], 'date': datetime.datetime.strptime(line['date'], '%Y-%m-%d').date(), })

new_data = [x for x in data if x['date'] <= (datetime.date.today() - timedelta(days=1))]


with open('reviews.csv', 'r') as rev:
    rev_reader = csv.DictReader(rev)
    reviews = []
    for line in rev_reader:
        reviews.append({'review': line['review'], 'name': line['name'], 'date': datetime.datetime.strptime(line['date'], '%Y-%m-%d').date(), 'image': line['image']})

new_reviews = [x for x in reviews if x['date'] <= (datetime.date.today() - timedelta(days=1))]