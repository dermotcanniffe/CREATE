# encoding: UTF-8
#from hamcrest import assert_that, equal_to, is_not
from hamcrest import *
import os.path
import yaml
import pytest
from munch import Munch
import create


class Actionwords:

    PROJECTROOT = os.curdir
    SETTINGSFILEPATH = PROJECTROOT+'/create.yaml'
    settingsfile = open(SETTINGSFILEPATH, 'r')

    def read_yaml(file_path):
        with open(file_path, "r") as f:
            return yaml.safe_load(f)

    myDict = read_yaml(SETTINGSFILEPATH)
    settings = Munch.fromDict(myDict)

    def __init__(self):
        pass

    def a_settings_file_is_in_an_expected_location(self):
        assert_that( (os.path.isfile(self.SETTINGSFILEPATH), True ) and ( self.settings.compositing.intro, is_not(empty)) and ( self.settings.compositing.outro, is_not(empty)))
        
    def we_run_the_application(self):
        assert_that( create.hello(), (True))


    def a_video_consisting_of_only_intro_and_outro_is_created(self):
        #assert(True is not True)
        pass

    def we_alter_the_settings_file(self):
        pass

    def a_video_consisting_of_a_new_intro_and_outro_is_created(self):
        pass
