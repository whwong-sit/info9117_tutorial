from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

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


@then('the system should identify the user')
def step_impl(context):
    """
    backend does its thing
    """
    pass

@then('refer the user to the personalized main screen')
def step_impl(context):
    with wait_for_page_load(context, 10):
        driver = context.browser
        title = driver.find_element_by_tag_name('title')
        user_id = driver.find_element_by_id('user_id')
        assert "Welcome" in title.text
        assert "test" in user_id.text

def wait_for_page_load(ctx, timeout=30):
    driver = ctx.browser
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until(
        staleness_of(old_page)
    )

