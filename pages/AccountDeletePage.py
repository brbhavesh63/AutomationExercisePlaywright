from playwright.sync_api import expect

from locators.accountdelete_page_locators import AccountDeletePageLocators


class AccountDeletedPage:

    def __init__(self,page):
        self.page = page

    def verifyAccountDeletePresent(self):
        expect(self.page.locator(AccountDeletePageLocators.ACCOUNT_DELETED)).to_have_text("Account Deleted!")

    def clickContinue(self):
        self.page.locator(AccountDeletePageLocators.CONTINUE_BTN).click()