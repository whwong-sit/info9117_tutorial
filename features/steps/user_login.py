from behave import *
from selenium import webdriver

@given('at the login screen')
def step_impl(ctx):
    """
    move selenium to login screen
    """
    driver = ctx.browser
    driver.get('http://localhost:8000/login')
    #assert "Login" in driver.page_source


@when('an existing user submits correct username and password')
def step_impl(ctx):
    """
    submit username and password
    """
    driver = ctx.browser
    username = driver.find_element_by_name("username")
    passwd = driver.find_element_by_name("password")
    username.send_keys("test")
    password.send_keys("test123")
    username.submit()


@then(u'the system should identify the user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should identify the user')

@then(u'refer the user to the personalized main screen')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then refer the user to the personalized main screen')