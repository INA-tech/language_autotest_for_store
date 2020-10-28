import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Choose language: ru, en-gb or es")

@pytest.fixture
def browser(request):
    content_language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': content_language})
    print(f"\nstart chrome browser for test on language {content_language}..")
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()

