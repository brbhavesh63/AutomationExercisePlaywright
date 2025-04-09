from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductsPage import ProductPage
from tests.conftest import browserInstance


def test_AddProductsToCart(browserInstance):

    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.NavigateToProducts()
    productpage = ProductPage(browserInstance)
    productpage.addProductsToCart()
    cartpage = CartPage(browserInstance)
    cartpage.verifyAddedCartProducts()
