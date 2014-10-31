from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    real_name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='profile_pictures',
        blank=True,
        null=True,
        default='profile_pictures/default-profile-photo.png')
    is_student = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{}".format(self.real_name) \
            if self.real_name \
            else u"{}".format(self.username) # prints out real_name or Username

"""
    am_pm input takes 1 small integer 2, 0, 1
    AM NOR PM equals 2
    AM equals 0
    PM equals 1
"""


class Slide(models.Model):
    name = models.CharField(max_length=150, null=True)
    week = models.IntegerField()
    day = models.CharField(max_length=150)
    am_pm = models.IntegerField()
    slide_number = models.IntegerField(help_text="index starts at 0")
    sub_slide_number = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)

    class Meta:
        unique_together = ("week", "day", "am_pm", "slide_number", "name")

    def url_construct(self):
        res_str = u"week{}/{}".format(self.week, self.day)

        if self.am_pm == 0:
            res_str += "_am"
        elif self.am_pm == 1:
            res_str += "_pm"

        res_str += "/#/{}".format(self.slide_number)

        if self.sub_slide_number:
            res_str += "/{}".format(self.sub_slide_number)

        return res_str

    def save(self, *args, **kwargs):
        self.url = self.url_construct()
        super(Slide, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return "{} - {}".format(self.url, self.name)


class Action(models.Model):
    done = models.BooleanField(default=False)
    need_help = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="actions")
    slide = models.ForeignKey(Slide, related_name="actions")
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"{}'s Action on slide {}".format(self.profile.first_name, self.slide.url)


class Question(models.Model):
    body = models.TextField()
    profile = models.ForeignKey(Profile, related_name="questions")
    slide = models.ForeignKey(Slide, related_name="questions")
    time = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)

    def __unicode__(self):
        return self.body
