import time

from behave import *
from Src.PageObject.Pages.Search import Search

use_step_matcher("re")

@then("Search")
def step_impl(context):
    Search.Search(context)

@then("Search Result Control and Go 2.Page")
def step_impl(context):
    Search.SearchResultControlgo2Page(context)