##pytest fixtures to avoid repetition of codes

import pytest
from selenium import webdriver
from utilities.loggerTest import Log_Maker
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",help="Specify browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    logger = Log_Maker.log_gen()
    logger.info(f"Initializing WebDriver for browser: {browser}")
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported Browser")
    return driver


##########for pytest html reports###########
##hook for adding custom environment info

def pytest_configure(config):
    config.stash[metadata_key]['Project Title']='Ecommerce Project, nopcommerce'
    config.stash[metadata_key]['TestModuleName']='Admin Login Test'

##hook for deleting unwanted env info####
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins',None)