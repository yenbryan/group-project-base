from HTMLParser import HTMLParser
import os
from slides.models import Slide
from bs4 import BeautifulSoup
from django.db.utils import IntegrityError


__author__ = 'GoldenGate'

from django.core.management import BaseCommand


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
                    # print day_am_pm
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
                        # for some reason, it returns -2 or -1 randomly
                        am_pm = -1
                        day = day_am_pm

                        print "day_am_pm " + str(day_am_pm)
                        print am_pm
                        print ""
                    self.run_soup(file_location, week, day, am_pm)

    def run_recursive_soup(self,location, week, day, am_pm):
        with open(location) as template:
            html = template.read()
            soup = BeautifulSoup(html)
            self.rec_parse(soup, week, day, am_pm)

    def run_soup(self, location, week, day, am_pm):
        with open(location) as template:
            html = template.read()
            soup = BeautifulSoup(html)
            slide_num = 0
            while(soup.find('section')):
                sub_num = 0
                slide_num += 1
                s = soup.find('section').extract()
                if s.contents[1].name == "section":
                    sub_1 = s.find('section').extract()
                    name = sub_1.find('h2')
                    self.savedata(str(name), week, day, am_pm, slide_num, sub_num)
                    while(s.find('section')):
                        sub_num += 1
                        sub = s.find('section').extract()
                        name = sub.find('h2')
                        self.savedata(str(name), week, day, am_pm, slide_num, sub_num)
                else:
                    name = s.find('h2')
                    self.savedata(str(name), week, day, am_pm, slide_num)

    def savedata(self, name, week, day, am_pm, slide_num, sub_num=None):
        name = BeautifulSoup(name).text
        if sub_num:
            try:
                Slide.objects.create(name=name, week=week, day=day, am_pm=am_pm, slide_number=slide_num, sub_slide_number=sub_num)
            except IntegrityError:
                pass
        else:
            try:
                Slide.objects.create(name=name, week=week, day=day, am_pm=am_pm, slide_number=slide_num)
            except IntegrityError:
                pass