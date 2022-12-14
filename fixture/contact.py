from model.contact import Contact

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
        #####################
        self.change_list_value("new_group", contact.new_group)
        #wd.find_element_by_name("new_group").click()
        # alternative- Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.new_group)
        #wd.find_element_by_xpath("//option[@value='"+contact.new_group+"']").click()
        self.fill_name_part3(contact)
        # enter secondary address
        self.fill_name_part2(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache=None

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
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
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
        #wd.implicitly_wait(5)
        self.app.open_home_page()
        self.contact_cache = None

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
        self.contact_cache = None

    def fill_name_part2(self, contact):
        wd = self.app.wd
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def fill_name_part3(self, contact):
        wd = self.app.wd
        # select b-date
        self.change_list_value("bday", contact.bday)
        self.change_list_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        # select a-date
        self.change_list_value("aday", contact.aday)
        self.change_list_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def change_list_value(self, list_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(list_name).click()
            wd.find_element_by_xpath("//option[@value='" + text + "']").click()

       #wd.find_element_by_name("new_group").click()
        # alternative- Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.new_group)
        #wd.find_element_by_xpath("//option[@value='"+contact.new_group+"']").click()


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        #return len (wd.find_elements_by_xpath("//input[@name='selected[]']"))
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache=[]
            #for element in wd.find_elements_by_name("entry"):
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                lname = element.find_elements_by_tag_name("td")[1].text
                fname = element.find_elements_by_tag_name("td")[2].text
                #lname = element.find_element_by_xpath("//*[@name='entry']/td[2]").text
                #print("lname", lname)
                #fname = element.find_element_by_xpath("//*[@name='entry']/td[3]").text
                #print("fname-", fname)
                id = element.find_element_by_name("selected[]").get_attribute("value")
                #print("id-",id)
                # id = element.find_element_by_xpath("//input[@name='selected[]']").get_attribute("value")
                self.contact_cache.append(Contact(firstname=fname, lastname=lname, id=id))
        return list(self.contact_cache)

