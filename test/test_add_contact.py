# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.creat_contact(Contact(firstname="Fname1", middlename="Mname1", lastname="Lname1", nickname="Nname1",
                                   title="qwerty1", company="asdfgh2", address="zxcvbnm3", home="111222", mobile="111333",
                                   workphone="111444", fax="111555", email="asd1@asd.asd", email2="asd2@asd.ad", email3="asd3@asd.asd",
                                   homepage="www.ya.ru", bday="1", bmonth="February", byear="1987", aday="2", amonth="April",
                                   ayear="2020", new_group="[none]", address2="zxzxzx", phone2="cvcvcv", notes="bnbnbn"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.creat_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                                   title="", company="", address="", home="", mobile="",
                                   workphone="", fax="", email="", email2="", email3="",
                                   homepage="", bday="", bmonth="-", byear="", aday="-", amonth="-",
                                   ayear="", new_group="[none]", address2="", phone2="", notes=""))
    app.session.logout()
