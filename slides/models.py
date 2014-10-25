from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    image = models.ImageField(
        upload_to='media/profile_picutures',
        blank=True,
        null=True)
    is_student = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)


class Slide(models.Model):
    week = models.IntegerField()
    day = models.IntegerField()
    am_pm = models.SmallIntegerField()
    slide_number = models.IntegerField()
    sub_slide_number = models.IntegerField(null=True, blank=True)
    url = models.URLField()

    def url_construct(self):
        res_str = ''
        if self.is_am == 0:
            res_str = "_am"
        elif self.am_pm == 1:
            res_str = "_pm"
        else:
            res_str = ""
        self.url = u"week{}/{}{}/#/{}/{} ".format(self.week, self.day, res_str, self.slide_number, self.sub_slide_number)

    def __unicode__(self):
        return self.url


class Action(models.Model):
    done = models.BooleanField(default=False)
    need_help = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="actions")
    slide = models.ForeignKey(Slide, related_name="actions")
    time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return self.done


class Question(models.Model):
    body = models.TextField()
    profile = models.ForeignKey(Profile, related_name="questions")
    slide = models.ForeignKey(Slide, related_name="questions")
    time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return self.body
