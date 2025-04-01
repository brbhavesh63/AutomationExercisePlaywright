from playwright.sync_api import expect, Page

from locators.home_page_locators import HomePageLocators
from pages.SignUpLoginPage import SignupLoginPage


class HomePage:

    def __init__(self,page : Page):
        self.page = page


    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def NavigateToSignupLoginPage(self):
        self.page.locator(HomePageLocators.SIGNUP_LOGIN_LINK).click()
        signup_login_page = SignupLoginPage(self.page)
        return signup_login_page

    def verifyTitle(self):
        act_title = self.page.title()
        print(act_title)
        # expect(act_title).to_have_text('Automation Exercise')
        assert act_title == 'Automation Exercise'

    def clickDeleteAccount(self):
        self.page.locator(HomePageLocators.DELETE_ACCOUNT_LINK).click()

    def clickLogout(self):
        self.page.locator(HomePageLocators.LOGOUT_LINK).click()

    def NavigateToContactUs(self):
        self.page.locator(HomePageLocators.CONTACTUS_LINK).click()

    def NavigateToTestCase(self):
        self.page.locator(HomePageLocators.TESTCASE_LINK).click()

    def NavigateToProducts(self):
        self.page.locator(HomePageLocators.PRODUCTS_LINK).click()

    def scrollToFooter(self):
        self.page.locator(HomePageLocators.FOOTER).scroll_into_view_if_needed()

    def subscribe(self,subscription_email):
        self.page.locator(HomePageLocators.SUBSCRIPTION_FIELD).fill(subscription_email)
        self.page.locator(HomePageLocators.SUBSCRIPTION_BTN).click()

    def verifySubscribSuccess(self):
        expect(self.page.locator(HomePageLocators.SUBSCRIBE_SUCCESS_MESSAGE)).to_have_text("You have been successfully subscribed!")


