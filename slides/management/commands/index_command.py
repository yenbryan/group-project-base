__author__ = 'GoldenGate'
from slides.models import Slide
from bs4 import BeautifulSoup
from django.db.utils import IntegrityError
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./slides/templates/') as template:
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
                        Slide.objects.create(name=str(header), week=week, day=day, am_pm=am_pm, slide_number=tracker)
                    except IntegrityError:
                        print "Integrity!!!!"
                    tracker += 1
                elif header != all_headers[(count-1)]:
                    try:
                        Slide.objects.create(name=str(header), week=week, day=day, am_pm=am_pm, slide_number=tracker)
                    except IntegrityError:
                        print "integrity!!!"
                    tracker += 1
                count += 1