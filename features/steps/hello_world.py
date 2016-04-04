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


@then("a welcome message is returned to the Visitor")
def step_impl(context):
   """
   Verify Hello World welcome message
   """
   assert "Hello World" in context.browser.page_source