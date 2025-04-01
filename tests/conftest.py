import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Launching Browser"
    )

@pytest.fixture(scope="session")
def register_data(request):
    return request.param

@pytest.fixture(scope="session")
def user_credential_data(request):
    return request.param

@pytest.fixture(scope="session")
def contact_us_data(request):
    return request.param

@pytest.fixture(scope="session")
def search_product_data(request):
    return request.param

@pytest.fixture(scope="session")
def subscription_data(request):
    return request.param

@pytest.fixture
def browserInstance(playwright,request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False, args=["--start-maximized"])

    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
    browser.close()


