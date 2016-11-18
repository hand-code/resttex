# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) 2016 by chenxiaofeng.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from datetime import datetime
from .base import db


class Love(db.Model):
    __tablename__ = 'love'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    shop_id = db.Column(db.Integer)

    create_time = db.Column(db.DateTime)

    user_id = db.Column(db.Integer)

    def __init__(self, shop_id, user_id):
        self.shop_id = shop_id
        self.user_id = user_id
        self.create_time = datetime.now()
