# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups=app.group.get_group_list()
    app.group.create(Group(gname="gr1", gheader="qwerty gr1", gfooter="asdfgh qr1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)

def test_add_empty_group(app):
    old_groups=app.group.get_group_list()
    app.group.create(Group(gname="", gheader="", gfooter=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
