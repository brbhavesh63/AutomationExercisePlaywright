import time

from playwright.sync_api import expect, Page

from locators.products_page_locators import ProductsPageLocators


class ProductPage:
    name_list = []
    price_list = []
    def __init__(self,page :Page):
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

    def addProductsToCart(self):
        totalHoverableItems = self.page.locator(ProductsPageLocators.TOTAL_PRODUCT_IMAGE_WRAPPER).count()
        print(totalHoverableItems)
        for i in range(totalHoverableItems+1):
            if i == 0 :
                continue
            self.page.locator(ProductsPageLocators.product_img_wrapper(i)).hover()
            overlay_product_price_list = self.page.locator(ProductsPageLocators.overlay_price_product(i)).text_content()
            overlay_product_name_list = self.page.locator(ProductsPageLocators.overlay_name_product(i)).text_content()
            self.name_list.append(overlay_product_name_list)
            self.price_list.append(overlay_product_price_list)
            self.page.locator(ProductsPageLocators.overlay_btn_addtocart(i)).click()
            if i == 1:
                self.page.locator(ProductsPageLocators.BTN_CONTINUE_SHOPPING).click()
            elif i == 2:
                self.page.locator(ProductsPageLocators.LINK_VIEW_CART).click()
                break