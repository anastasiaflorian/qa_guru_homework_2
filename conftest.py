import pytest
from selene.support.shared import browser

@pytest.fixture(autouse=True)
def open_browser():
    browser.open("https://www.google.com")

    yield

    browser.quit()

@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080