from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase
from slides.utils import handle
from slides.models import Slide, Profile, Action


class ViewTestCase(TestCase):

    def setUp(self):
        handle()
        self.teacher = Profile.objects.create_user(
            username="teacher",
            password="teacher",
            is_student=False,
            real_name="teacher",
            email="test@test.com")
        self.student = Profile.objects.create_user(
            username='student',
            email='student@test.com',
            password='student',
            is_student=False,
            real_name="student",)
        self.client.login(username="teacher", password="teacher")

    def test_teacher_page(self):
        # self.client.login(username="teacher", password="teacher")
        # response = self.client.get(reverse('slides_home'))
        response = self.client.get(reverse('teacher',
                                           kwargs={
                                               'week': '1',
                                               'day': '1',
                                               'am_pm': '2'}))
        self.assertIn('<h4 class="week-info">Week 1 - 1</h4>', response.content)

    def test_teacher_help(self):
        response = self.client.get(reverse('teacher_help',
                                           kwargs={
                                               'slide_url': 'week1/1/#/1',}))
        self.assertIn('<img class="icon" src="/static/img/Assets/Exclamation-hollow.png" alt=""/>', response.content)

    def test_teacher_done(self):
        response = self.client.get(reverse('teacher_done',
                                           kwargs={
                                               'slide_url': 'week1/1/#/1',}))
        self.assertIn('<img class="icon" src="/static/img/Assets/Checkmark-HOLLOW.png" alt=""/>', response.content)

    def test_teacher_question(self):
        response = self.client.get(reverse('teacher_question',
                                           kwargs={
                                               'slide_url': 'week1/1/#/1',}))
        self.assertIn('<img class="icon" src="/static/img/Assets/Questionmark-hollow.png" alt=""/>', response.content)

