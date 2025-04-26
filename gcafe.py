import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
# Specify the path to your local ChromeDriver executable
chromedriver_path = '/Users/vonuyvico/Downloads/chromedriver-mac-arm64/chromedriver'  # Update this path accordingly
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open your target website
driver.get("http://captive.apple.com")

def generate_num():
    """Generate a six-digit random number as a string."""
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

try:
    while True:
        # Generate a random six-digit number
        random_number = generate_num()

        # Wait until the input field is present and then interact with it
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-input'))
        )
        current_value = input_field.get_attribute('value')
        for _ in range(len(current_value)):
            input_field.send_keys(Keys.BACKSPACE)
        input_field.send_keys(random_number)
        print("Input value:", random_number)

        # Wait until the button is clickable, then click it
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-area.ant-btn'))
        )
        button.click()
        print("Button clicked")

        # Wait for 30 milliseconds before repeating
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Process interrupted by user.")
finally:
    driver.quit()
