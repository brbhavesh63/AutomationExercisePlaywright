import json

import pytest

from pages.HomePage import HomePage
from pages.SignUpLoginPage import SignupLoginPage

with open("C:\\Users\\Bhavesh\\PycharmProjects\\AutomationExercise\\data\\login_valid_data.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]
    print(user_credentials_list)

@pytest.mark.parametrize('user_credential_data',user_credentials_list)
def test_LoginValidUser(user_credential_data,browserInstance):

    user_email = user_credential_data["user_email"]
    user_password = user_credential_data["user_password"]

    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.NavigateToSignupLoginPage()

    signuploginpage = SignupLoginPage(browserInstance)
    signuploginpage.setLoginEmail(user_email)
    signuploginpage.setLoginPassword(user_password)
    signuploginpage.clickLogin()
    homepage.verifyTitle()

