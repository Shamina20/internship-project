from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application


def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """

    context.driver = webdriver.Firefox()


    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # context.driver = webdriver.Chrome(
    #     options=options
    # )


    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
