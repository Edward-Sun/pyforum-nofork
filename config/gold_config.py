#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'
import os
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'website/static/')

# 端口配置
API_PORT = 15102
ADMIN_PORT = 15103

# Blueprint配置
WWW_URL_PREFIX = '/www'
ADMIN_URL_PREFIX = ''
M_URL_PREFIX = '/m'

FLASK_PORT = 5000

# 服务器地址
M_ADDRESS = 'http://localhost:'+str(FLASK_PORT)+'/m/'
API_ADDRESS = 'http://localhost:'+str(FLASK_PORT)+'/v2/api'

SUPER_ADMIN = ('admin', 'admin')


# 数据库配置
MYSQL_NAME = 'pyforum'
MYSQL = {'host': 'localhost', 'password': '123456', 'user': 'root'}

OBJECT_ID_WIDTH = 10 ** 13  # 全局ID的长度

# 日志配置
# LOG_SILENT = True
LOG_SILENT = False

TEMPLATES_AUTO_RELOAD =True #自动刷新html

# REDIS_HOST = '139.162.78.193'
# REDIS_PORT = '6479'
# REDIS_DB = '8'
# REDIS_PASSWORD = 'walkerpassw0rd'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6380'
REDIS_DB = '8'
REDIS_PASSWORD = ''


# SESSION
SESSION_SALT = 'h\xf2\x80-\x93\x80\x9d\x8b\xdf_\t\xa4>5\xa2w\x91\xcd\xe1\x82\xdb\xde\x18\xfe'

APP_MODE = 'DEV'

# email server
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'pythonforum@163.com'
MAIL_PASSWORD = 'python163'
MAIL_DEFAULT_SENDER = 'pythonforum@163.com'
#MAIL_SUPPRESS_SEND = True  # 为True时,不会发送邮件


SECRET_KEY = '6a4c8iu7fa'