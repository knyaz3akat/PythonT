class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Creat new group
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.gname)
        self.change_field_value("group_header", group.gheader)
        self.change_field_value("group_footer", group.gfooter)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        wd = self.app.wd
        # Open group page
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # Select 1th group
        # alternative: wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//span[@class='group']/input[@name='selected[]']").click()
        # Submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_first_group(self, group_data):
        wd = self.app.wd
        self.open_group_page()
        # Select 1th group
        wd.find_element_by_xpath("//span[@class='group']/input[@name='selected[]']").click()
        # Submit edit
        wd.find_element_by_name("edit").click()
        # Fill group
        self.fill_group_form(group_data)
        # Submit Update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len (wd.find_elements_by_xpath("//span[@class='group']/input[@name='selected[]']"))
