# common.py
from selenium import webdriver
from behave import given, when, then
import time



def launch_browser(context, browser):
    browser = browser.lower()

    if browser == "chrome":
        context.driver = webdriver.Chrome()
    elif browser == "firefox":
        context.driver = webdriver.Firefox()
    elif browser == "edge":
        context.driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser type: {browser}")

    context.driver.maximize_window()
    time.sleep(2)

def open_orange_hrm_url(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
