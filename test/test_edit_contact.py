from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Fname001", middlename="Mname001", lastname="Lname001", nickname="Nname001",
                               title="qwerty001", company="asdfgh002", address="zxcvbnm003", home="111000222", mobile="111000333",
                               workphone="111000444", fax="111000555", email="asd01@asd.asd", email2="asd02@asd.ad", email3="asd03@asd.asd",
                               homepage="www.ya1.ru", bday="8", bmonth="March", byear="1980", aday="10", amonth="July",
                               ayear="2010", new_group="", address2="zxz000xzx", phone2="cvc000vcv", notes="bnb000nbn"))
    app.session.logout()

