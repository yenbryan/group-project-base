from slides.models import Slide

__author__ = 'GoldenGate'

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        x = ["bryan", "peter"]
        for names in x:
            print names
Slide.objects.create(week=1, day=1, am_pm=-1, slide_number=0)