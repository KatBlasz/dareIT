import os
import unittest
from selenium import webdriver
import time

from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_player import AddPlayer

class TestFillForm(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        super(TestFillForm, self).setUp(self)

    def test_fill_in_player_form(self):
        TestLoginPage.test_login_to_the_system(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player()
        add_player = AddPlayer(self.driver)
        add_player.type_in_email('marian@amorki.pl')
        add_player.type_in_name('Marian')
        add_player.type_in_surname('Drozd')
        add_player.type_in_phone('123456')
        add_player.type_in_weight('80kg')
        add_player.type_in_height('180')
        add_player.type_in_main_position('Napastnik')
        add_player.click_add_link_to_youtube()
        add_player.type_in_youtube_link('https://www.youtube.com/watch?v=Go-jJlGd1so&pp=ygUheW91IHdpbGwgbmV2ZXIgd2FsayBhbG9uZSBhbmZpZWxk')
        add_player.type_in_main_club('Liverpool')
        add_player.type_in_level('Advanced')
        add_player.type_in_achievements('brak')
        add_player.type_in_second_position('Bramkarz')
        add_player.click_on_the_language_button()
        add_player.type_in_language('English')
        add_player.click_on_the_choose_leg_button()
        add_player.click_on_the_right_leg()
        time.sleep(5)

    def test_submit_form(self):
        add_player = AddPlayer(self.driver)
        add_player.click_on_the_submit()

    @classmethod
    def tearDown(self):
        self.driver.quit()


pass