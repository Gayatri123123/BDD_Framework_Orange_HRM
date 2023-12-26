import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver


@given('I lauched chrome browser')
def lanch_browser(context):
    context.driver = webdriver.Chrome()

@when(u'I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    time.sleep(2)

@when(u'Enter username "{username}" and password "{password}"')
def step_impl(context,username,password):
    context.driver.find_element(By.XPATH,"//*[@name='username']").send_keys(username)
    context.driver.find_element(By.XPATH,"//*[@name='password']").send_keys(password)

@when(u'clicks on Login button')
def step_impl(context):
   context.driver.find_element(By.XPATH,"//*[@type='submit']").click()

@then(u'user should get logged in to dashboard page')
def step_impl(context):
    time.sleep(5)
    text = context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
    assert text == 'Dashboard'
    context.driver.close()

@when(u'click on Admin button')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()


@then(u'highlight the System users')
def step_impl(context):
    time.sleep(3)
    ele=context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5')
    context.driver.execute_script("arguments[0].style.color='yellow'",ele)
    time.sleep(5)
