from playwright.sync_api import expect

from locators.search_page_locators import SearchPageLocators
class SearchPage:

    def __init__(self,page):
        self.page = page

    def verifySearchedProductVisible(self,searched_product_name):
        expect(self.page.locator(SearchPageLocators.SEARCHED_PRODUCT_NAME)).to_have_text(searched_product_name)
