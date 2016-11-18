# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) 2016 by chenxiaofeng.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

from .base import db


class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(128))

    # 经度
    longitude = db.Column(db.Float)

    # 纬度
    latitude = db.Column(db.Float)

    # 照片
    pics = db.Column(db.String(128))

    # 介绍
    description = db.Column(db.Text)

    # 点赞业务信息 #

    # 点赞数
    love_number = db.Column(db.Integer)

    def __init__(self, user_id, name, pics, longitude=0.0, latitude=0.0, description=''):
        self.user_id = user_id
        self.name = name
        self.pics = pics
        self.longitude = longitude
        self.latitude = latitude
        self.description = description
