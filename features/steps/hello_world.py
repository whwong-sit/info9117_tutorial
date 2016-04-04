from behave import *

use_step_matcher("re")


@given("The system is running")
def step_impl(context):
    pass


@when("a Visitor visits the landing page")
def step_impl(context):
    """
    Visit the landing page
    """
    context.browser.get(context.address)
    context.response = context.browser.page_source


@then('"Hello World" is returned to the Visitor')
def step_impl(context, text="Hello World"):
    """
    :type context: behave.runner.Context
    """
    if text not in context.response:
        fail('%r not in %r' % (text, context.response))
