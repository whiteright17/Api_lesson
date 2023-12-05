import pytest
from selenium_all import MySelenium


@pytest.fixture()
def my_selenium_fixture(request):
    my_selenium = MySelenium()
    my_selenium.get_page("https://www.google.com")
    yield my_selenium
    my_selenium.driver.quit()
