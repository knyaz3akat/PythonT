class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        ### fill contact form
        self.fill_name_part1(contact)
        ## select group
        wd.find_element_by_name("new_group").click()
        # alternative- Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.new_group)
        wd.find_element_by_xpath("//option[@value='"+contact.new_group+"']").click()
        # enter secondary address
        self.fill_name_part2(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def fill_name_part1(self, contact):
        wd = self.app.wd
        # enter First name
        self.change_field_value("firstname", contact.firstname)
        # enter Middle name
        self.change_field_value("middlename", contact.middlename)
        # enter Last name
        self.change_field_value("lastname", contact.lastname)
        # enter Nickname
        self.change_field_value("nickname", contact.nickname)
        # enter title
        self.change_field_value("title", contact.title)
        # enter company
        self.change_field_value("company", contact.company)
        # enter address company
        self.change_field_value("address", contact.address)
        ### enter Telephone
        # enter home phone
        self.change_field_value("home", contact.homephone)
        # enter mobile
        self.change_field_value("mobile", contact.mobile)
        # enter work phone
        self.change_field_value("work", contact.workphone)
        # enter fax
        self.change_field_value("fax", contact.fax)
        # enter e-mail
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Select 1th contact
        self.select_first_contact()
        # Submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='selected[]']").click()

    def edit_first_contact(self, new_contact_date):
        wd = self.app.wd
        self.app.open_home_page()
        # Select 1th contact
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        ### fill contact form
        self.fill_name_part1(new_contact_date)
        """ field 'groups' is missing """
        self.fill_name_part3(new_contact_date)
        ## enter secondary address
        self.fill_name_part2(new_contact_date)
        ##
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.return_to_home_page()

    def fill_name_part2(self, contact):
        wd = self.app.wd
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def fill_name_part3(self, contact):
        wd = self.app.wd
        # select b-date
        wd.find_element_by_name("bday").click()
        # alternative- crash test  Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath("//option[@value='" + contact.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        # alternative- crash test  Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath("//option[@value='" + contact.bmonth + "']").click()
        self.change_field_value("byear", contact.byear)
        # select a-date
        wd.find_element_by_name("aday").click()
        # alternative-  Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_xpath("//select[@name='aday']/option[text()='" + contact.aday + "']").click()
        wd.find_element_by_name("amonth").click()
        # alternative-  Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_xpath("//select[@name='amonth']/option[text()='" + contact.amonth + "']").click()
        self.change_field_value("ayear", contact.ayear)
