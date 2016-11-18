# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) 2016 by chenxiaofeng.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

from models.base import db
from models.love import Love


def add_love(shop_id, user_id):
    love = Love(shop_id, user_id)
    db.session.add(love)
    db.session.commit()
