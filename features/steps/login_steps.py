from behave import *
from pages.login_page import LoginPage


@given('user launches the application')
def step_impl(context):
    context.driver.get("https://automationexercise.com/")
    context.login_page = LoginPage(context.driver)


@when('user enters valid email and password')
def step_impl(context):

    print("Entering login details")
    context.login_page.open_login()
    context.login_page.enter_email()
    context.login_page.enter_password()
    context.login_page.click_login()


@then('user should be logged in successfully')
def step_impl(context):

    print("Login successful")
    assert context.login_page.verify_login()