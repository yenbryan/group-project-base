__author__ = 'GoldenGate'

import os
from slides.models import Slide
from bs4 import BeautifulSoup
from django.db.utils import IntegrityError
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
                # constructing file path location and parsing the path with parameters
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

    # take location of decks and loop over each to create individual slides
    def run_soup(self, location, week, day, am_pm):
        with open(location) as template:
            html = template.read()
            first_tag = html.replace("{% block presentation_title %}","<div id='topic'>")
            second_tag = first_tag.replace("{% endblock %}","</div>")
            soup2 = BeautifulSoup(second_tag)
            topic = soup2.find("div", {"id": "topic"}).get_text().lstrip()
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
            # create slide unless its already been created (checked by unique together in models)
            for header in all_headers:
                if count == 0:
                    try:
                        print header
                        Slide.objects.create(name=str(header), week=week, day=day, am_pm=am_pm, slide_number=tracker, topic=topic)
                    except IntegrityError:
                        print "Integrity!!!!"
                    tracker += 1
                elif header != all_headers[(count-1)]:
                    try:
                        print header
                        Slide.objects.create(name=str(header), week=week, day=day, am_pm=am_pm, slide_number=tracker, topic=topic)
                    except IntegrityError:
                        print "integrity!!!"
                    tracker += 1
                count += 1