from . import views
from django.contrib import messages
import configparser
import os
import json

def read_ini(filename, infoName):
    cfgpath = os.path.join(filename)
    # 创建管理对象
    conf = configparser.ConfigParser()
    # 读ini文件
    conf.read(cfgpath, encoding = 'utf-8')
    return dict(conf[infoName])

def read_txt(filename):
    info = open(filename, "r")
    data = info.readlines()
    return list(data)

def read_json(filename):
    f = open(filename, encoding = 'utf-8')
    data = json.load(f)
    return data

def message(request, text):
    messages.success(request, text)