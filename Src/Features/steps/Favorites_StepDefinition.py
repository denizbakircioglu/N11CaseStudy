import time

from behave import *
from Src.PageObject.Pages.Favorites import Favorites

use_step_matcher("re")

@then("Add to favorites of the first 3 products")
def step_impl(context):
    Favorites.AddFavorite3Product(context)

@then("Add Favorites")
def step_impl(context):
    Favorites.goToFavorites(context)

@then("Delete Favorites")
def step_impl(context):
    Favorites.DeleteFavoriteProduct(context)
