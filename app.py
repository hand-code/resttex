# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) 2016 by chenxiaofeng.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)
