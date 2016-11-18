# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) 2016 by chenxiaofeng.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

from .base import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=120))
    # 密码的hash值
    password = db.Column(db.String(length=128))
    qq = db.Column(db.String(length=20))
    mobile = db.Column(db.String(length=11))

    def __init__(self, name, password, mobile, qq=None):
        self.name = name
        self.password = password
        self.mobile = mobile
        self.qq = qq
