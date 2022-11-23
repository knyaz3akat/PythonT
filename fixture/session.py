

class SessionHelper:
    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        # Authorization
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        # Exit
        wd.find_element_by_link_text("Logout").click()
        #wd.find_element_by_name("user").clear()
        #wd.find_element_by_name("user").send_keys("admin")
