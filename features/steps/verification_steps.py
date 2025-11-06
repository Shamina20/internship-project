from behave import given, when, then
from time import sleep

@then('Verify the right page opens')
def verify_right_page(context):
    context.app.verification_page.verify_page()
    sleep(1)


@then('Verify each product on this page contains a title and a visible picture')
def verify_title_and_visible_picture(context):
    context.app.verification_page.verify_title_and_visible_picture()

    print(context.driver.execute_script("return navigator.userAgent;"))