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
        with open('./slides/templates/week1/1.html') as f:
            html = f.read()
            soup = BeautifulSoup(html)
            sections = soup.find_all('section')
            # print sections
            all_headers = []
            for header in sections:
                instance = str((header.find('h2')))
                instance = instance[4:]
                instance = instance[:-5]
                all_headers.append(instance)
            print all_headers
            


            # print all_headers
        #     parser = MyHTMLParser()
        #     parser.feed(html)
