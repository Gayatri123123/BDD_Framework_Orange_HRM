import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver


@given('I lauched browser chrome')
def lanch_browser(context):
    context.driver = webdriver.Chrome()

@when(u'I open orange HRM page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    time.sleep(2)

@when(u'Enter username "{username}" and password "{password}" fields')
def step_impl(context,username,password):
    context.driver.find_element(By.XPATH,"//*[@name='username']").send_keys(username)
    context.driver.find_element(By.XPATH,"//*[@name='password']").send_keys(password)

@when(u'clicks on Login')
def step_impl(context):
   context.driver.find_element(By.XPATH,"//*[@type='submit']").click()

@then(u'user should get logged into Dashboard Page of HRM')
def step_impl(context):
    time.sleep(5)
    text = context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
    assert text == 'Dashboard'
    context.driver.close()

