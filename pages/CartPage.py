from playwright.sync_api import Page

from locators.cart_page_locators import CartPageLocators
from pages.ProductsDetailPage import ProductsDetailsPage
from pages.ProductsPage import ProductPage


class CartPage:

    def __init__(self,page:Page):
        self.page = page
        self.name_row_list = []
        self.price_row_list = []

    def verifyAddedCartProducts(self):

        totalNoOfRows = self.page.locator(CartPageLocators.NUMBER_OF_ROWS).count()

        for i in range(totalNoOfRows+1):
            if i==0:
                continue
            row_product_name = self.page.locator(CartPageLocators.product_name(i)).text_content()
            row_product_price = self.page.locator(CartPageLocators.product_price(i)).text_content()
            self.name_row_list.append(row_product_name)
            self.price_row_list.append(row_product_price)

        assert self.name_row_list == ProductPage.name_list and self.price_row_list == ProductPage.price_list


    def verifyQty(self,qty):
        cart_qty = self.page.locator(CartPageLocators.QTY).text_content()
        assert  cart_qty == qty
