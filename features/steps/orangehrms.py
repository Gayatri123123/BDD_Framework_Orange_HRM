import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By



@given('luanch the browser')
def lanch_browser(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    time.sleep(2)


@then('Verify logo present on page')
def verify_logo(context):
   time.sleep(3)
   status = context.driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[1]/img').is_displayed()
   assert status is True
   ele = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/h5')
   context.driver.execute_script("arguments[0].style.color='yellow'",ele)
   time.sleep(5)

@then('close browser')
def close_browser(context):
    context.driver.close()
