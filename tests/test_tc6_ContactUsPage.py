import json

import pytest

from pages.ContactUsPage import ContactusPage
from pages.HomePage import HomePage

with open("C:\\Users\\Bhavesh\\PycharmProjects\\AutomationExercise\\data\\contact_us_data.json") as f:
    test_data = json.load(f)
    contact_us_list = test_data["contact_us_details"]

@pytest.mark.parametrize('contact_us_data',contact_us_list)
def test_ContactUsDetails(contact_us_data,browserInstance):

    contactus_name = contact_us_data["contactus_name"]
    contactus_email = contact_us_data["contactus_email"]
    contactus_subject = contact_us_data["contactus_subject"]
    contactus_message = contact_us_data["contactus_message"]

    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.NavigateToContactUs()

    contactuspage = ContactusPage(browserInstance)
    contactuspage.verifyGetInTouchVisiblity()
    contactuspage.setContactUsDetails(contactus_name,contactus_email,contactus_subject,contactus_message)
    contactuspage.clickSubmit()
    contactuspage.verifySubmitSuccessMessage()


