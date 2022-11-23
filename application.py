from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def logout(self):
        wd = self.wd
        # Exit
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")

    def return_to_group_page(self):
        wd = self.wd
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def creat_group(self, group):
        wd = self.wd
        self.open_group_page()
        # Creat new group
        wd.find_element_by_name("new").click()
        # Fill group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.gname)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.gheader)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.gfooter)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.wd
        # Open group page
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.wd
        # Open home page
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        # Authorization
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def destroy(self):
        self.wd.quit()