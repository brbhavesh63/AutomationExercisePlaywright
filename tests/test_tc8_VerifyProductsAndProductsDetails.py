from pages.HomePage import HomePage
from pages.ProductsDetailPage import ProductsDetailsPage
from pages.ProductsPage import ProductPage


def test_verifyProductsDetails(browserInstance):
    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.NavigateToProducts()

    productpage = ProductPage(browserInstance)
    productpage.verifyHeaderVisible()
    productpage.verifyProductsListVisibility()
    productpage.clickFirstProduct()

    productdetailpage = ProductsDetailsPage(browserInstance)
    productdetailpage.verifyTitle()
    productdetailpage.verifyProductsDetailsVisibility()
