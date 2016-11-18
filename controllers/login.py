# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) 2016 by chenxiaofeng.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from app import app
from actions import loveaction


@app.route('/', methods=['post', 'get'])
def hello_world():
    loveaction.add_love(200, 200)
    return 'Hello World!'
