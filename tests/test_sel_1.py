import pytest
from selenium_all import MySelenium


@pytest.fixture
def selenium_instance():
    selenium = MySelenium()
    yield selenium
    selenium.driver.quit()


def test_base_url(my_selenium_fixture):
    my_selenium_fixture.follow_links_and_return()
    assert my_selenium_fixture.driver.current_url == "https://www.google.com/"
    expected_text = "google"
    assert expected_text in my_selenium_fixture.driver.title.lower()
