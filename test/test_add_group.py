# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(gname="gr1", gheader="qwerty gr1", gfooter="asdfgh qr1"))
    app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(gname="", gheader="", gfooter=""))
    app.session.logout()
