from django.contrib import admin
from slides.models import Profile, Slide, Action, Question

admin.site.register(Profile)
admin.site.register(Slide)
admin.site.register(Action)
admin.site.register(Question)