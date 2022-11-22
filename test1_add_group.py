# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group1 import Group1

class test1_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test1_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.creat_group(wd, Group1(gname="gr1", gheader="qwerty gr1", gfooter="asdfgh qr1"))
        self.logout(wd)

    def test1_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.creat_group(wd, Group1(gname="", gheader="", gfooter=""))
        self.logout(wd)

    def logout(self, wd):
        # Exit
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")

    def return_to_group_page(self, wd):
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def creat_group(self, wd, group1):
        self.open_group_page(wd)
        # Creat new group
        wd.find_element_by_name("new").click()
        # Fill group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group1.gname)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group1.gheader)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group1.gfooter)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page(wd)

    def open_group_page(self, wd):
        # Open group page
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self, wd):
        # Open home page
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        self.open_home_page(wd)
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        # Authorization
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


