from behave import *

# This should be added to environment.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords()

use_step_matcher('re')


@then(r'A video consisting of a new Intro and Outro is created')
def impl(context):
    context.actionwords.a_video_consisting_of_a_new_intro_and_outro_is_created()


@then(r'A video consisting of only Intro and Outro is created')
def impl(context):
    context.actionwords.a_video_consisting_of_only_intro_and_outro_is_created()


@given(r'a Settings file is in an expected location')
def impl(context):
    context.actionwords.a_settings_file_is_in_an_expected_location()


@when(r'we alter the settings file')
def impl(context):
    context.actionwords.we_alter_the_settings_file()


@when(r'we run the application')
def impl(context):
    context.actionwords.we_run_the_application()
