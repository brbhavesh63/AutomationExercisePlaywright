from locators.register_page_locators import RegisterPageLocators


class RegisterPage:

    def __init__(self,page):
        self.page = page

    def setPassword(self,password):
        self.page.locator(RegisterPageLocators.PASSWORD).fill(password)

    def selectBirthDate(self,day,month,year):
        self.page.locator(RegisterPageLocators.SELECT_DAYS).select_option(day)
        self.page.locator(RegisterPageLocators.SELECT_MONTHS).select_option(month)
        self.page.locator(RegisterPageLocators.SELECT_YEARS).select_option(year)

    def checkNewsletterOffers(self):
        self.page.locator(RegisterPageLocators.CHECK_NEWSLETTER).click()
        self.page.locator(RegisterPageLocators.CHECK_OFFER).click()

    def setAddressInfo(self,firstname,lastname,company,address,country,state,city,zipcode,mobile):
        self.page.locator(RegisterPageLocators.FIRSTNAME).fill(firstname)
        self.page.locator(RegisterPageLocators.LASTNAME).fill(lastname)
        self.page.locator(RegisterPageLocators.COMPANY).fill(company)
        self.page.locator(RegisterPageLocators.ADDRESS).fill(address)
        self.page.locator(RegisterPageLocators.SELECT_COUNTRY).select_option(country)
        self.page.locator(RegisterPageLocators.STATE).fill(state)
        self.page.locator(RegisterPageLocators.CITY).fill(city)
        self.page.locator(RegisterPageLocators.ZIPCODE).fill(zipcode)
        self.page.locator(RegisterPageLocators.MOBILE).fill(mobile)

    def clickCreateAccount(self):
        self.page.locator(RegisterPageLocators.CLICK_CREATEACCOUNT).click()