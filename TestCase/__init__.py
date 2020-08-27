# coding = utf-8

# -*- coding:utf8 -*-

# coding：gbk
# coding：utf-8
# -*-coding：gbk-*-


import unittest
from TestCase.main_entrance import *
from logging_handler import Logger
from global_attributes import lvp_project_path

lvp = PumpLibrary.main()

log = Logger(lvp_project_path + 'TestLog/test_process_log.csv', level='debug')
log_error = Logger(lvp_project_path + '/TestLog/test_process_log_error.csv', level='error')
