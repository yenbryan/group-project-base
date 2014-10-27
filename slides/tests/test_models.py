from django.test import TestCase
from slides.models import Profile, Slide, Action, Question


class ModelTestCase(TestCase):

    def setUp(self):
        self.profile = Profile.objects.create(
            username="test",
            password="test",
            email="test@test.com",
            first_name='test',
            last_name='test',
            real_name = 'test test')
        self.slide = Slide.objects.create(
            week=1,
            day=1,
            am_pm=1,
            slide_number=1,
            sub_slide_number=1)
        self.action = Action.objects.create(profile=self.profile, slide=self.slide)
        self.question = Question.objects.create(body="This working?", profile=self.profile, slide=self.slide)

    def test_profile_creation(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(self.profile.__unicode__(), "test test")

    def test_url_construct(self):
        self.assertEqual(self.slide.url_construct(), 'week1/1_pm/#/1/1')

        # URL construction when there isn't a subslide
        slides_without_subslides = Slide.objects.create(
            week=1,
            day=1,
            am_pm=1,
            slide_number=1)
        self.assertEqual(slides_without_subslides.url_construct(), 'week1/1_pm/#/1')

    def test_slide_creation(self):
        self.assertTrue(isinstance(self.slide, Slide))
        self.assertEqual(self.slide.__unicode__(), self.slide.url)

    def test_action_creation(self):
        self.assertTrue(isinstance(self.action, Action))
        self.assertEqual(self.action.__unicode__(), "test's Action on slide week1/1_pm/#/1/1")

    def test_question_creation(self):
        self.assertTrue(isinstance(self.question, Question))
        self.assertEqual(self.question.__unicode__(), self.question.body)