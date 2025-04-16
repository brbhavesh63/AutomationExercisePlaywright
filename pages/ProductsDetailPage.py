from playwright.sync_api import expect

from locators.productsdetails_page_locators import ProductsDetailsPageLocators


class ProductsDetailsPage:

    def __init__(self,page,qty):
        self.page = page
        self.qty = qty

    def verifyTitle(self):
        act_title = self.page.title()
        assert act_title == "Automation Exercise - Product Details"

    def verifyProductsDetailsVisibility(self):
        expect(self.page.locator(ProductsDetailsPageLocators.PRODUCT_NAME)).to_be_visible()
        expect(self.page.locator(ProductsDetailsPageLocators.PRODUCT_CATEGORY)).to_be_visible()
        expect(self.page.locator(ProductsDetailsPageLocators.PRODUCT_PRICE)).to_be_visible()
        expect(self.page.locator(ProductsDetailsPageLocators.PRODUCT_AVAILABILITY)).to_be_visible()
        expect(self.page.locator(ProductsDetailsPageLocators.PRODUCT_BRAND)).to_be_visible()
        expect(self.page.locator(ProductsDetailsPageLocators.PRODUCT_CONDITION)).to_be_visible()

    def setQty(self):
        self.page.locator(ProductsDetailsPageLocators.QTY_FIELD).fill(self.qty)

    def clickAddToCart(self):
        self.page.locator(ProductsDetailsPageLocators.ADDTOCART_BTN).click()

    def clickViewCart(self):
        self.page.locator(ProductsDetailsPageLocators.VIEWCART_LINK).click()
