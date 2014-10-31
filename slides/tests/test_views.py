from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase
from slides.utils import handle
from slides.models import Slide, Profile, Action, Question


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

    def test_registration(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'password1': 'test',
            'password2': 'test',
            'real_name': 'test',
        }
        response = self.client.post(reverse('register'), data)

        # Check this user was created in the database
        # self.assertTrue(Player.objects.filter(username=username).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('slides_home')))

    def test_registration_form_page(self):
        response = self.client.get(reverse('register'))
        self.assertIn('<div id="registration_form" class="col-md-3">', response.content)

    def test_send_action_done(self):
        data = '{"week":"1","day":"1","am_pm":"2","slide_number":"1","text":""}'
        response = self.client.post(reverse('new_action',kwargs={'action': 2}),
                                    content_type='application/json', data=data)
        self.assertTrue(Action.objects.filter(done=True).exists())


    def test_send_action_question(self):
        data = '{"week":"1","day":"1","am_pm":"2","slide_number":"1","text":"question is here"}'
        response = self.client.post(reverse('new_action',kwargs={'action': 3}),
                                    content_type='application/json', data=data)
        self.assertTrue(Question.objects.filter(body="question is here").exists())

    def test_send_action_need_help(self):
        data = '{"week":"1","day":"1","am_pm":"2","slide_number":"1","text":""}'
        response = self.client.post(reverse('new_action',kwargs={'action': 1}),
                                    content_type='application/json', data=data)
        self.assertTrue(Action.objects.filter(need_help=True).exists())


    def test_account_page(self):
        response = self.client.get(reverse('account'))
        self.assertIn('<a href="">Upload a new profile photo</a>', response.content)

    def test_edit_name(self):
        self.client.login(username="student", password="student")
        data = '{"test": "edit"}'
        response = self.client.post(reverse('edit_name'),
                                    content_type='application/json', data=data)

        self.assertEqual(Profile.objects.get(username="student").real_name, u"{u'test': u'edit'}")