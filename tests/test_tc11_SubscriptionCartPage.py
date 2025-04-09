import json

import pytest

from pages.HomePage import HomePage


with open("C:\\Users\\Bhavesh\\PycharmProjects\\AutomationExercise\\data\\subscription_email_data.json") as f:

    test_data = json.load(f)
    subscription_email_list = test_data["subscription_email_data"]
@pytest.mark.parametrize('subscription_data',subscription_email_list)
def test_AddProductsInCart(subscription_data,browserInstance):
    subscription_email = subscription_data["subscription_email"]
    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.NavigateToCarts()
    homepage.scrollToFooter()
    homepage.subscribe(subscription_email)
    homepage.verifySubscribSuccess()


