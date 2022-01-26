import time

from behave import *
from Src.PageObject.Pages.Login import Login

use_step_matcher("re")

@step("Open Login Page")
def step_impl(context):
    Login.goToLogin(context)
    time.sleep(2)

@then("Login")
def step_impl(context):
    Login.Login(context)
    time.sleep(2)
