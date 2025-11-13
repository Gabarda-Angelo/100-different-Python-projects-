import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the cookie clicker game
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for the game to load
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# Record start time
start_time = time.time()
playing = True

while playing:
    try:
        # Click the big cookie continuously
        cookie_button = driver.find_element(By.ID, "bigCookie")
        cookie_button.click()

        # Check elapsed time
        elapsed = time.time() - start_time

        # Every 5 seconds, try to buy the best product(You can change the number of seconds to save alot of cookies before buying)
        if elapsed >= 60:
            print("1 minute have passed!")
            start_time = time.time()

            # Re-fetch elements **every time** to avoid stale references
            enabled_products = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")

            if enabled_products:
                # Get the most expensive product — last in the list
                best_product = enabled_products[-1]

                # Get name safely before clicking
                product_name = best_product.text.split("\n")[0].strip()

                # If the product name is empty, skip it
                if product_name:
                    best_product.click()
                    print(f"Bought: {product_name}")
                else:
                    print("Skipped buying: Empty product name")
            else:
                print("No affordable products yet...")

    except StaleElementReferenceException:
        print("Stale element detected. Retrying...")
        # Small sleep to allow DOM refresh, then retry
        time.sleep(0.5)
        continue
