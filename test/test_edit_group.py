from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(gname="gr3-edit", gheader="qwerty gr3-edit", gfooter="asdfgh qr3-edit"))
    app.session.logout()

