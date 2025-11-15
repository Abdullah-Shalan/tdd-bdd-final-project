"""
Environment for Behave Testing
"""
from os import getenv
from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '30'))
BASE_URL = getenv('BASE_URL', 'http://localhost:8080')
DRIVER = getenv('DRIVER', 'firefox').lower()


def before_all(context):
    """ Executed once before all tests """
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS

    # Headless Firefox options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service, options=options)



def after_all(context):
    """ Executed after all tests """
    context.driver.quit()


    