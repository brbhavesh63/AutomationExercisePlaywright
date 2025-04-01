from playwright.sync_api import expect

from locators.accountcreate_page_locators import AccountCreatePageLocators


class AccountCreatePage:

    def __init__(self,page):
        self.page = page

    def verifyAccountCreatePresent(self):
        expect(self.page.locator(AccountCreatePageLocators.ACCOUNT_CREATE)).to_have_text("Account Created!")

    def clickContinue(self):
        self.page.locator(AccountCreatePageLocators.CONTINUE_BTN).click()
