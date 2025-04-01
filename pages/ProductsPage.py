from playwright.sync_api import expect

from locators.products_page_locators import ProductsPageLocators


class ProductPage:

    def __init__(self,page):
        self.page = page

    def verifyHeaderVisible(self):
        expect(self.page.locator(ProductsPageLocators.ALLPRODUCTS_HEADER)).to_have_text("All Products")

    def verifyProductsListVisibility(self):
        expect(self.page.locator(ProductsPageLocators.FEATURE_ITEMS)).to_be_visible()

    def clickFirstProduct(self):
        self.page.locator(ProductsPageLocators.FIRST_PRODUCT).click()

    def searchProducts(self,search_name):
        self.page.locator(ProductsPageLocators.SEARCH_FIELD).fill(search_name)
        self.page.locator(ProductsPageLocators.SEARCH_BTN).click()
