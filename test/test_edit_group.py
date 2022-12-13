from model.group import Group

def test_edit_first_group(app):
    if app.group.count()==0:
        app.group.create(Group(gname="GN_test"))

    old_groups=app.group.get_group_list()
    app.group.edit_first_group(Group(gname="gr3-edit", gheader="qwerty gr3-edit", gfooter="asdfgh qr3-edit"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_name(app):
    if app.group.count()==0:
        app.group.create(Group(gname="GN_test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(gname="New gr3-edit"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    if app.group.count()==0:
        app.group.create(Group(gname="GN_test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(gheader="New qwerty"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
