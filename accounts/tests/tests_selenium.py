from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('window-size=1920x1080')


# Create your tests here.
class UserFormTest(StaticLiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(
            executable_path=str('accounts/tests/chromedriver.exe'),
            options=chrome_options, )
        self.selenium.implicitly_wait(30)
        self.selenium.maximize_window()

    def test_form(self):
        # Choose your url to visit
        self.selenium.get(str(self.live_server_url) + "/accounts/register/")
        # find the elements you need to submit form
        username = self.selenium.find_element_by_name('username')
        email = self.selenium.find_element_by_name('email')
        password1 = self.selenium.find_element_by_name('password1')
        password2 = self.selenium.find_element_by_name('password2')

        submit = self.selenium.find_element_by_name('input_register')

        # populate the form with data
        username.send_keys('selenium')
        email.send_keys('selenium@hotmail.com')
        password1.send_keys('selenium')
        password2.send_keys('selenium')

        # submit form
        submit.click()
        time.sleep(1)
