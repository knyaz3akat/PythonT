from random import randrange
from model.contact import Contact


def test_edit_contact_by_index(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Fname4Test"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    #print("4ucJlo 1 = " + str(index))
    contact=Contact(firstname="Fname003еее", middlename="Mname003кккк", lastname="Lname003ннннн", nickname="Nname003",
                                           title="qwerty001", company="asdfgh002", address="zxcvbnm003", homephone="111000222", mobile="111000333",
                                           workphone="111000444", fax="111000555", email="asd01@asd.asd", email2="asd02@asd.ad", email3="asd03@asd.asd",
                                           homepage="www.ya1.ru", bday="8", bmonth="March", byear="1980", aday="10", amonth="July",
                                           ayear="2010", new_group="", address2="zxz000xzx", phone2="cvc000vcv", notes="bnb000nbn")
    contact.id=old_contact[index].id
    #app.contact.edit_first_contact(contact)
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index]=contact
    assert len(old_contact) == len(new_contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


"""
def test_edit_first_contact(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Fname4Test"))
    old_contact = app.contact.get_contact_list()
    contact=Contact(firstname="Fname003", middlename="Mname003", lastname="Lname003", nickname="Nname003",
                                           title="qwerty001", company="asdfgh002", address="zxcvbnm003", homephone="111000222", mobile="111000333",
                                           workphone="111000444", fax="111000555", email="asd01@asd.asd", email2="asd02@asd.ad", email3="asd03@asd.asd",
                                           homepage="www.ya1.ru", bday="8", bmonth="March", byear="1980", aday="10", amonth="July",
                                           ayear="2010", new_group="", address2="zxz000xzx", phone2="cvc000vcv", notes="bnb000nbn")
    contact.id=old_contact[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[0]=contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_edit_first_contact_fname(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Fname4Test"))
    old_contact = app.contact.get_contact_list()
    contact=Contact(firstname="Fname004")
    contact.id=old_contact[0].id
    app.contact.edit_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0]=contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_edit_first_contact_lname(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="Fname4Test"))
    old_contact = app.contact.get_contact_list()
    contact=Contact(lastname="Lname004")
    contact.id=old_contact[0].id
    app.contact.edit_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0]=contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
"""