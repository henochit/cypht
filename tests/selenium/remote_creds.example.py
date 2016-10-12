#!/usr/bin/python

# This is an example config file to run the Selenium tests remotely,
# specifically with BrowserStack (https://www.browserstack.com) 

# Get webdrivers
from selenium import webdriver

# Define the webdriver to use
DRIVER = webdriver.Remote

# Define the remote command. This format is specific to browserstack.com
DRIVER_CMD='http://<yourcreds>@hub.browserstack.com:80/wd/hub'

# Set the browser and OS attributes
DESIRED_CAP = {'os': 'Windows', 'os_version': '7', 'browser': 'IE', 'browser_version': '11', 'resolution': '1920x1080' }

# The base URL to run the tests against
SITE_URL = 'https://some-public-site-running-cypht.com'

# A valid username to login with
USER = 'testuser'

# A valid password for the username
PASS = 'testpass'

# A function that returns a webdriver object.
def get_driver():
    return DRIVER(command_executor=DRIVER_CMD, desired_capabilities=DESIRED_CAP)