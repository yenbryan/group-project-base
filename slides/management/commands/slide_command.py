from HTMLParser import HTMLParser
from slides.models import Slide
from bs4 import BeautifulSoup


__author__ = 'GoldenGate'

from django.core.management import BaseCommand


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "section":
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "SCRIPT!!!!!!!"
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data


class Command(BaseCommand):
    def handle(self, *args, **options):
        # x = ["bryan", "peter"]
        # for names in x:
        #     print names
        # Slide.objects.create(week=1, day=1, am_pm=-1, slide_number=0)
        week = 1
        day = 1
        with open('./slides/templates/week'+str(week)+'/'+str(day)+'.html') as f:
            html = f.read()
            soup = BeautifulSoup(html)
            sections = soup.find_all('section')
            all_headers = []
            for header in sections:
                instance = str((header.find('h2')))
                instance = instance[4:]
                instance = instance[:-5]
                all_headers.append(instance)
            print all_headers
            count = 0
            tracker = 1
            for header in all_headers:
                if count == 0:
                    Slide.objects.create(name=str(header), week=week, day=day, am_pm=-1, slide_number=tracker)
                    print "created header at count" + str(count)
                    print header
                    tracker += 1
                elif header != all_headers[(count-1)]:
                    Slide.objects.create(week=week, day=day, am_pm=-1, slide_number=(tracker))
                    print "created header at count" + str(count)
                    print header
                    tracker += 1
                count += 1