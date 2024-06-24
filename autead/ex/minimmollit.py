from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up the Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window on startup
chrome_options.add_argument("--disable-extensions")  # Disable browser extensions

# Set up the Chrome service
chrome_service = Service('/path/to/chromedriver')  # Replace with the actual path to the chromedriver executable

# Create a new Chrome driver with the options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
