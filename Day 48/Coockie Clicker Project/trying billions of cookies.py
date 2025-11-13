import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the cookie clicker game
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for the big cookie to appear
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# 🔹 Wait until the Game object exists in JavaScript
WebDriverWait(driver, 30).until(
    lambda d: d.execute_script("return typeof Game !== 'undefined' && Game.ready")
)

# 💡 Give yourself Trillions of cookies instantly AFTER the game initializes
driver.execute_script("Game.cookies = 999_000_000_000_000")
print("💰 Successfully gave you 10 billion cookies!")

# Record start time
start_time = time.time()
buy_interval = 5
playing = True

while playing:
    try:
        # Click the big cookie continuously
        cookie_button = driver.find_element(By.ID, "bigCookie")
        cookie_button.click()

        # Check elapsed time
        elapsed = time.time() - start_time

        # Every 5 seconds, try to buy the best product
        if elapsed >= buy_interval:
            print(f"{buy_interval} seconds Buying interval reached! Checking upgrades...")
            start_time = time.time()

            # Re-fetch elements every time to avoid stale references
            enabled_products = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")

            if enabled_products:
                best_product = enabled_products[-1]
                product_name = best_product.text.split("\n")[0].strip()

                if product_name:
                    # Click product & move mouse away to avoid tooltip overlap
                    best_product.click()
                    driver.execute_script("document.querySelector('#tooltip').style.display='none';")
                    print(f"Bought: {product_name}")
                else:
                    print("Skipped buying: Empty product name")
            else:
                print("No affordable products yet...")

            buy_interval += buy_interval

    except StaleElementReferenceException:
        print("Stale element detected. Retrying...")
        time.sleep(0.5)
        continue

    except ElementClickInterceptedException:
        print("Tooltip blocked the cookie! Hiding tooltip...")
        driver.execute_script("document.querySelector('#tooltip').style.display='none';")
        time.sleep(0.2)
        continue
