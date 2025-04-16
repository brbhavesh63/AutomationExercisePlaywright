import time

from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductsDetailPage import ProductsDetailsPage


def test_VerifyProductQtyInCart(browserInstance,qty):
    # qty = "4"
    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.scrollDownToFirstProduct()
    homepage.clickFirstProduct()
    productdetailspage = ProductsDetailsPage(browserInstance,qty)
    productdetailspage.verifyTitle()
    productdetailspage.setQty()
    productdetailspage.clickAddToCart()
    time.sleep(2)
    productdetailspage.clickViewCart()
    cartpage = CartPage(browserInstance)
    cartpage.verifyQty(qty)