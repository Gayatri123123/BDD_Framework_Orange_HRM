import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver
#from common import open_orange_hrm_url


@given('I lauched the browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when(u'I open orange HRM Homepage')
def launch_orange_hrm_page(context):
    #open_orange_hrm_url(context)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)


@when(u'Enter username "{username}" and password "{password}"')
def enter_user_credentail(context,username,password):
    context.driver.find_element(By.XPATH,"//*[@name='username']").send_keys(username)
    context.driver.find_element(By.XPATH,"//*[@name='password']").send_keys(password)

@when(u'clicks on Login button')
def click_on_login_btn(context):
   context.driver.find_element(By.XPATH,"//*[@type='submit']").click()

@then(u'user should get logged into dashboard page')
def verifying_dashboard_page(context):
    time.sleep(5)
    text = context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')
    context.driver.execute_script("arguments[0].style.color='yellow'",text)
    #assert text == 'Dashboard'
    time.sleep(3)
    context.driver.close()

@when(u'click on Admin button')
def click_on_admin_btn(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()


@then(u'highlight the System users')
def highlight_system_user(context):
    time.sleep(3)
    ele=context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5')
    context.driver.execute_script("arguments[0].style.color='yellow'",ele)
    time.sleep(5)
'''

@when(u'Enter Invalid username "{username}" and password "{password}"')
def enter_user_Invalid_credentail(context,username,password):
    context.driver.find_element(By.XPATH,"//*[@name='username']").send_keys(username)
    context.driver.find_element(By.XPATH,"//*[@name='password']").send_keys(password)
'''

@when(u'Enter Invalid username "abc" and password "abc123"')
def enter_user_Invalid_credentail(context):
    context.driver.find_element(By.XPATH,"//*[@name='username']").send_keys("abc")
    context.driver.find_element(By.XPATH,"//*[@name='password']").send_keys("abc123")

@then(u'user should get proper error message')
def verfying_invalid_credentials(context):
    time.sleep(2)
    ele=context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]')
    context.driver.execute_script("arguments[0].style.color='yellow'",ele)
    time.sleep(5)
