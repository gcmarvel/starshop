from django import template
import random

register = template.Library()

from ..tabledata import new_reviews


@register.inclusion_tag('randomreview.html')
def random_review():
    x = len(new_reviews)
    indexlist = random.sample(range(x), 6)
    reviewset1 = new_reviews[indexlist[0]]
    review1 = reviewset1.get('review')
    name1 = reviewset1.get('name')
    date1 = reviewset1.get('date')
    image1 = reviewset1.get('image')
    reviewset2 = new_reviews[indexlist[1]]
    review2 = reviewset2.get('review')
    name2 = reviewset2.get('name')
    date2 = reviewset2.get('date')
    image2 = reviewset2.get('image')
    reviewset3 = new_reviews[indexlist[2]]
    review3 = reviewset3.get('review')
    name3 = reviewset3.get('name')
    date3 = reviewset3.get('date')
    image3 = reviewset3.get('image')
    reviewset4 = new_reviews[indexlist[3]]
    review4 = reviewset4.get('review')
    name4 = reviewset4.get('name')
    date4 = reviewset4.get('date')
    image4 = reviewset4.get('image')
    reviewset5 = new_reviews[indexlist[4]]
    review5 = reviewset5.get('review')
    name5 = reviewset5.get('name')
    date5 = reviewset5.get('date')
    image5 = reviewset5.get('image')
    reviewset6 = new_reviews[indexlist[5]]
    review6 = reviewset6.get('review')
    name6 = reviewset6.get('name')
    date6 = reviewset6.get('date')
    image6 = reviewset6.get('image')
    return {'review1': review1, 'name1': name1, 'date1': date1, 'image1': image1, 'review2': review2, 'name2': name2, 'date2': date2, 'image2': image2,
            'review3': review3, 'name3': name3, 'date3': date3, 'image3': image3, 'review4': review4, 'name4': name4, 'date4': date4, 'image4': image4,
            'review5': review5, 'name5': name5, 'date5': date5, 'image5': image5, 'review6': review6, 'name6': name6, 'date6': date6, 'image6': image6,}


