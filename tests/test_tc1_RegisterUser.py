import json

import pytest
from playwright.sync_api import Playwright

from pages.AccountCreatePage import AccountCreatePage
from pages.AccountDeletePage import AccountDeletedPage
from pages.HomePage import HomePage
from pages.SignUpLoginPage import SignupLoginPage
from pages.UserRegisterPage import RegisterPage


with open("C:\\Users\\Bhavesh\\PycharmProjects\\AutomationExercise\\data\\register_user_data.json") as f:
    register_data = json.load(f)
    register_data_list = register_data["register_user"]
    print(register_data_list)



@pytest.mark.parametrize('register_data',register_data_list)
def test_RegisterUser(register_data,browserInstance):
        signup_name = register_data["signup_name"]
        signup_email = register_data["signup_email"]
        password = register_data["password"]
        day = register_data["day"]
        month = register_data["month"]
        year = register_data["year"]
        firstname = register_data["first_name"]
        lastname = register_data["last_name"]
        company = register_data["company"]
        address = register_data["address"]
        country = register_data["country"]
        state = register_data["state"]
        zipcode = register_data["zipcode"]
        city = register_data["city"]
        mobile = register_data["mobile"]

        homepage = HomePage(browserInstance)
        homepage.navigate()
        homepage.verifyTitle()
        homepage.NavigateToSignupLoginPage()

        signuploginpage = SignupLoginPage(browserInstance)
        signuploginpage.verifySignupFormHeader()
        signuploginpage.setSignupName(signup_name)
        signuploginpage.setSignupEmail(signup_email)
        signuploginpage.clickSignup()

        userrgisterpage = RegisterPage(browserInstance)
        userrgisterpage.setPassword(password)
        userrgisterpage.selectBirthDate(day,month,year)
        userrgisterpage.checkNewsletterOffers()
        userrgisterpage.setAddressInfo(firstname,lastname,company,address,country,state,city,zipcode,mobile)
        userrgisterpage.clickCreateAccount()

        accountcreatepage = AccountCreatePage(browserInstance)
        accountcreatepage.verifyAccountCreatePresent()
        accountcreatepage.clickContinue()

        homepage.clickDeleteAccount()

        accountdeletepage = AccountDeletedPage(browserInstance)
        accountdeletepage.verifyAccountDeletePresent()
        accountdeletepage.clickContinue()







