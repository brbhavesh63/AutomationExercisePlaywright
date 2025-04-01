from playwright.sync_api import expect

from locators.signup_login_page_locators import SignUpLoginPageLocators
from pages import UserRegisterPage
class SignupLoginPage:


    def __init__(self,page):
        self.page = page

    def verifySignupFormHeader(self):
        header = self.page.locator(SignUpLoginPageLocators.SIGNUP_FORM_HEADER)
        expect(header).to_have_text("New User Signup!")

    def setSignupName(self,signupname):
        self.page.locator(SignUpLoginPageLocators.SIGNUP_NAME).fill(signupname)

    def setSignupEmail(self,signupemail):
        self.page.locator(SignUpLoginPageLocators.SIGNUP_EMAIL).fill(signupemail)

    def clickSignup(self):
        self.page.locator(SignUpLoginPageLocators.SIGNUP_BTN).click()

    def setLoginEmail(self,loginemail):
        self.page.locator(SignUpLoginPageLocators.LOGIN_EMAIL).fill(loginemail)

    def setLoginPassword(self,loginpassword):
        self.page.locator(SignUpLoginPageLocators.LOGIN_PASSWORD).fill(loginpassword)

    def clickLogin(self):
        self.page.locator(SignUpLoginPageLocators.LOGIN_BTN).click()

    def verifyInvalidLoginValidationError(self):
        expect(self.page.locator(SignUpLoginPageLocators.LOGIN_VALIDATION_MSG)).to_have_text("Your email or password is incorrect!")

    def verifyAlreadyExistingUserValidationError(self):
        expect(self.page.locator(SignUpLoginPageLocators.SIGNUP_VALIDATION_MSG)).to_have_text("Email Address already exist!")

