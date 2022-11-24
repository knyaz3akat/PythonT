from model.group import Group

#def test_edit_first_group(app):
#    app.group.edit_first_group(Group(gname="gr3-edit", gheader="qwerty gr3-edit", gfooter="asdfgh qr3-edit"))
#    app.session.logout()

def test_edit_group_name(app):
    app.group.edit_first_group(Group(gname="New gr3-edit"))
    app.session.logout()

def test_edit_group_header(app):
    app.group.edit_first_group(Group(gheader="New qwerty"))
    app.session.logout()
