from django.contrib import admin

# Register your models here.
from slides.models import Profile, Slide, Question, Action

admin.site.register(Slide)
admin.site.register(Question)
admin.site.register(Action)
admin.site.register(Profile)
