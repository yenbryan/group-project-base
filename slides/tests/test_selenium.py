from slides.management.commands.slide_command import Command

__author__ = 'GoldenGate'

from time import sleep
from django.core.urlresolvers import reverse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from slides.models import Profile, Slide, Action, Question
from django.test import LiveServerTestCase


class SeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        Profile.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')
        super(SeleniumTests, cls).setUpClass()
        Command()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_admin_login(self):
        # Create a superuser
        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
        self.selenium.find_element_by_name('username').send_keys('superuser')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('mypassword')

        # Submit the form
        password_input.send_keys(Keys.RETURN)
        # sleep for half a second to let the page load
        sleep(.5)


        # We check to see if 'Site administration' is now on the page, this means we logged in successfully
        # body = self.selenium.find_element_by_tag_name('body')
        # self.assertIn('Site administration', body.text)

    def admin_login(self):
        # Create a superuser
        Profile.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')

        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))

        # let's fill out the form with our superuser's username and password
        self.selenium.find_element_by_name('username').send_keys('superuser')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('mypassword')

        # Submit the form
        password_input.send_keys(Keys.RETURN)

    # Only works if you comment out the above code because you are trying to login twice
    # or you can tell selenium to log itself out
    def test_register(self):
        self.selenium.get("{}{}".format(self.live_server_url, reverse('slides_home')))
        self.selenium.find_element_by_id('registerButton').click()
        self.selenium.find_element_by_id('id_username').send_keys("selenium")
        self.selenium.find_element_by_id('id_password1').send_keys("my_password")
        self.selenium.find_element_by_id('id_password2').send_keys("my_password")
        self.selenium.find_element_by_id('id_real_name').send_keys("Selenium Tester")
        self.selenium.find_element_by_id('email').send_keys("selenium@gmail.com")
        # self.selenium.find_element_by_id('submit-id-register').click()
        self.selenium.find_element_by_css_selector("input[value='Register']").click()
        sleep(12)