from pages.HomePage import HomePage
from tests.conftest import browserInstance


def test_TestCasePage(browserInstance):

    homepage = HomePage(browserInstance)
    homepage.navigate()
    homepage.verifyTitle()
    homepage.NavigateToTestCase()
