from HTMLParser import HTMLParser
import os
from slides.models import Slide
from bs4 import BeautifulSoup
from django.db.utils import IntegrityError


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
        # return directories where slide decks live
        walker = os.walk('./slides/templates/')
        # navigating to individual slide decks
        for folder in walker:
            index1 = folder[0]
            index = index1[-5:]
            index = index[:-1]
            # print folder
            if index == "week":
                files = folder[2]
                for file in files:
                    file_location = str(folder[0]) + "/" + str(file)
                    week = index1[-1]
                    day_am_pm = file[:-5]
                    if day_am_pm[-3:] == "_am":
                        am_pm = 0
                        day = day_am_pm[:1]
                        print "day_am_pm " + str(day_am_pm)
                        print am_pm
                        print ""
                    elif day_am_pm[-3:] == "_pm":
                        am_pm = 1
                        day = day_am_pm[:1]
                        print "day_am_pm " + str(day_am_pm)
                        print am_pm
                        print ""
                    else:
                        am_pm = 2
                        day = day_am_pm
                        print "day_am_pm " + str(day_am_pm)
                        print am_pm
                        print ""
                    self.run_soup(file_location, week, day, am_pm)

    def run_soup(self, location, week, day, am_pm):
        with open(location) as template:
            html = template.read()
            soup = BeautifulSoup(html)
            sections = soup.find_all('section')
            all_headers = []
            for header in sections:
                instance = str((header.find('h2')))
                instance = instance[4:]
                instance = instance[:-5]
                all_headers.append(instance)
            count = 0
            tracker = 1
            for header in all_headers:
                if count == 0:
                    try:
                        print ""
                        Slide.objects.create(name=str(header), week=week, day=day, am_pm=am_pm, slide_number=tracker)
                    except IntegrityError:
                        print "Integrity!!!!"
                    tracker += 1
                elif header != all_headers[(count-1)]:
                    try:
                        print ""
                        Slide.objects.create(name=str(header), week=week, day=day, am_pm=am_pm, slide_number=tracker)
                    except IntegrityError:
                        print "integrity!!!"
                    tracker += 1
                count += 1