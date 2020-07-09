from django.shortcuts import render
from django.http import HttpResponse
import requests
import zipfile
import csv
from io import TextIOWrapper
from websites.models import Website, WebsiteCategory


# Create your views here.
def ad_to_db(rank, url):

    get_category = WebsiteCategory.objects.get(pk=1)

    website = Website()
    website.alexa_rank = rank
    website.url = url
    website.save()

    website.category.add(get_category)
    website.save()


def get_write(request):
    r = requests.get('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    with open('data_zip', 'wb') as f:
        f.write(r.content)

    with zipfile.ZipFile('data_zip', 'r') as data_zip:
        with data_zip.open('top-1m.csv') as csv_file:
            reader = csv.reader(TextIOWrapper(csv_file, 'utf-8'))
            counter = 0
            for row in reader:
                print(row)
                get_rank = row[0]
                get_url = row[1]
                ad_to_db(get_rank, get_url)
                counter += 1

            return HttpResponse('Counter: ', counter)
