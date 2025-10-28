from time import sleep

from behave import given, when, then

@given('Open the main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(4)


@when('User logs in with {email} and {password}')
def user_log_in(context,email,password):
    context.app.main_page.user_login(email,password)
    sleep(10)



