from behave import given, when, then
from time import sleep

@when('Click on “off plan” at the left side menu')
def click_off_plan(context):
    context.app.offplan_page.click_off_plan()
    sleep(4)

