
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture
def launch_browser(context):
    # Launch Browser
    # print("=============>Browser is created")
    chrome_options = Options()
    chrome_options.add_argument("--disable-features=CookiesWithoutSameSiteMustBeSecure,SameSiteByDefaultCookies,#CookiesWithoutSameSiteMustBeSecure;")
    chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-extensions-file-access-check")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    context.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/driver/chromedriver.exe')
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    yield context.driver



@fixture
def quit_browser(context):
    # Clean Up Browser
    context.driver.quit()
    # print("=============>Browser is quit")


def before_scenario(context, scenario):
    the_fixture1 = use_fixture(launch_browser, context)


def after_scenario(context, scenario):
    the_fixture2 = use_fixture(quit_browser, context)

# def after_step(context, step):
#    if step.name == "Login to the backoffice":
#        HomePage.changeLanguage(context, "EN")
