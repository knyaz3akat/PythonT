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

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Select 1th group
        wd.find_element_by_xpath("//span[@class='group']/input[@name='selected[]']").click()
        # Submit edit
        wd.find_element_by_name("edit").click()
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
        # Submit Update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
