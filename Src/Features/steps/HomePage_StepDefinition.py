import time

from behave import *
from Src.PageObject.Pages.Favorites import Favorites
from Src.PageObject.Pages.Home import Home

use_step_matcher("re")

@given("Home Page")
def step_impl(context):
    Home.goToHome(context)