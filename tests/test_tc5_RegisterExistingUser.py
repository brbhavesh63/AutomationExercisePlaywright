import json

import pytest

from pages.HomePage import HomePage
from pages.SignUpLoginPage import SignupLoginPage

with open("C:\\Users\\Bhavesh\\PycharmProjects\\AutomationExercise\\data\\register_user_data.json") as f:
    test_data = json.load(f)
    register_data_list = test_data["register_user"]
    print(register_data_list)


@pytest.mark.parametrize("register_data",register_data_list)
def test_RegisterExistingUser(register_data,browserInstance):

    signup_existing_email = register_data["signup_existing_email"]
    signup_name = register_data["signup_name"]

    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.NavigateToSignupLoginPage()

    signuploginpage = SignupLoginPage(browserInstance)
    signuploginpage.verifySignupFormHeader()
    signuploginpage.setSignupName(signup_name)
    signuploginpage.setSignupEmail(signup_existing_email)
    signuploginpage.clickSignup()
    signuploginpage.verifyAlreadyExistingUserValidationError()
