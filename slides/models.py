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
        return u"(), {}".format(self.username, self.real_name)
    # if there isn't a first and last name return username

"""
    am_pm input takes 1 small integer -1, 0, 1
    AM NOR PM equals -1
    AM equals 0
    PM equals 1
"""


class Slide(models.Model):
    week = models.IntegerField()
    day = models.IntegerField()
    am_pm = models.SmallIntegerField()
    slide_number = models.IntegerField()
    sub_slide_number = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=150)

    def url_construct(self):
        res_str = ''
        if self.am_pm == 0:
            res_str = "_am"
        elif self.am_pm == 1:
            res_str = "_pm"
        else:
            res_str = ""
        return u"week{}/{}{}/#/{}/{}".format(self.week, self.day, res_str, self.slide_number, self.sub_slide_number)

    def save(self, *args, **kwargs):
        self.url = self.url_construct()
        super(Slide, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return self.url


class Action(models.Model):
    done = models.BooleanField(default=False)
    need_help = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="actions")
    slide = models.ForeignKey(Slide, related_name="actions")
    time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return u"{}'s Action on slide {}".format(self.profile.first_name, self.slide.url)


class Question(models.Model):
    body = models.TextField()
    profile = models.ForeignKey(Profile, related_name="questions")
    slide = models.ForeignKey(Slide, related_name="questions")
    time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return self.body
