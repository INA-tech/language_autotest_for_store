import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.unit
def test_btn_store(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket").is_displayed(), \
        'Кнопка добавления товара отсутствует'
    time.sleep(10)