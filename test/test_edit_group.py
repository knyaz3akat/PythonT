from model.group import Group

def test_edit_first_group(app):
    if app.group.count()==0:
        app.group.create(Group(gname="GN_test"))
    app.group.edit_first_group(Group(gname="gr3-edit", gheader="qwerty gr3-edit", gfooter="asdfgh qr3-edit"))


def test_edit_group_name(app):
    if app.group.count()==0:
        app.group.create(Group(gname="GN_test"))
    app.group.edit_first_group(Group(gname="New gr3-edit"))


def test_edit_group_header(app):
    if app.group.count()==0:
        app.group.create(Group(gname="GN_test"))
    app.group.edit_first_group(Group(gheader="New qwerty"))

