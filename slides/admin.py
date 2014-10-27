from django.contrib import admin
from slides.models import Profile, Slide, Question, Action, SlideDeck

admin.site.register(Slide)
admin.site.register(Question)
admin.site.register(Action)
admin.site.register(Profile)
admin.site.register(SlideDeck)
