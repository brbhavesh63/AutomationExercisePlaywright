import json
import time

import pytest

from pages.HomePage import HomePage
from pages.ProductsPage import ProductPage
from pages.SearchPage import SearchPage

with open("C:\\Users\\Bhavesh\\PycharmProjects\\AutomationExercise\\data\\search_product_data.json") as f:

    test_data = json.load(f)
    search_product_list = test_data["search_data"]
    print(search_product_list)

@pytest.mark.parametrize('search_product_data',search_product_list)
def test_verifySearchedProducts(search_product_data,browserInstance):

    search_product_name = search_product_data["search_product_name"]

    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.NavigateToProducts()

    product = ProductPage(browserInstance)
    product.searchProducts(search_product_name)

    searchpage = SearchPage(browserInstance)
    searchpage.verifySearchedProductVisible(search_product_name)
