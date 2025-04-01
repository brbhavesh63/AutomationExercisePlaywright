import time

from playwright.sync_api import expect

from locators.contactus_page_locators import ContactUsPageLocators


class ContactusPage:

    def __init__(self,page):
        self.page = page

    def verifyGetInTouchVisiblity(self):
        expect(self.page.locator(ContactUsPageLocators.GETINTOUCH_HEADER)).to_have_text("Get In Touch")

    def setContactUsDetails(self,contactusname,contactusemail,contactussubject,contactusmessage):
        self.page.locator(ContactUsPageLocators.CONTACT_NAME).fill(contactusname)
        self.page.locator(ContactUsPageLocators.CONTACT_EMAIL).fill(contactusemail)
        self.page.locator(ContactUsPageLocators.CONTACT_SUBJECT).fill(contactussubject)
        self.page.locator(ContactUsPageLocators.CONTACT_MESSAGE).fill(contactusmessage)

    def clickSubmit(self):
        # Listening to alert first
        self.page.on("dialog", lambda dialog : dialog.accept())
        time.sleep(3)
        self.page.locator(ContactUsPageLocators.SUBMIT_BTN).click()

    def verifySubmitSuccessMessage(self):
        expect(self.page.locator(ContactUsPageLocators.SUBMIT_SUCCESS_MESSAGE)).to_have_text("Success! Your details have been submitted successfully.")
