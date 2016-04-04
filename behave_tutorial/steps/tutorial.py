from behave import *

@given('we have behave installed')
def step_impl(ctx):
    pass

@when('we implement a test')
def step_impl(ctx):
    assert True is not False

@then('behave will test it for us')
def step_impl(ctx):
    assert ctx.failed is False
