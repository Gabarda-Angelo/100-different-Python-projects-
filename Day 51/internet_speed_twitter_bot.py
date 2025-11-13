from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 10
X_EMAIL = "gelo.gabarda@gmail.com"
X_PASSWORD = "15minuterule"
X_USERNAME= "Gelociouss"
SPEED_TEST_URL ="https://www.speedtest.net/"
X_URL = "https://x.com/"


class InternetSpeedTwitterBot:
    def __init__(self):
        # Keep Chrome browser open after program finishes
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.download = 0
        self.upload = 0


    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        wait = WebDriverWait(self.driver, 60)
        try:
            go_button = wait.until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')))
            go_button.click()
            print("clicked successful!")

            try:
                #wait this element to appear, indicating that the data we wanted(upload/download data) is available now
                data_available = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[4]/div/div/div[2]/div/div/h3')))

                # text_content = data_available.text.strip()
                if data_available:
                    print("Data is available!")
                    # print("Text:", text_content)
                    isp_data_download_text = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
                    isp_data_upload_text = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))

                    self.download = float(isp_data_download_text.text.strip())
                    self.upload = float(isp_data_upload_text.text.strip())

                    print(f"Download Speed: {self.download} Mbps")
                    print(f"Upload Speed: {self.upload} Mbps")
                else:
                    print("Element found, but it's empty.")
            except TimeoutException:
                print("time out, Session expired.")
                exit()

        except (ElementClickInterceptedException or TimeoutException):
            print("Time out or Couldn't find element!")
            pass

    def tweet_at_provider(self):
        self.driver.get(X_URL)

        wait = WebDriverWait(self.driver, 60)


        try:
            sign_in_button = wait.until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a')))
            sign_in_button.click()

            if sign_in_button:
                # Wait for the email input field to be visible and interactable
                email_input_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))

                # Clear any existing text (optional, but recommended)
                email_input_field.clear()

                # putting text in input field
                email_input_field.send_keys(X_EMAIL)

                #next button click
                next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')))
                next_button.click()

                # Wait for the username input field to be visible and interactable
                username_input_field = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))

                # Clear any existing text
                username_input_field.clear()

                # putting text in input field
                username_input_field.send_keys(X_USERNAME)

                # next button click
                next_button_un = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')))
                next_button_un.click()


                # Wait for the password input field to be visible and interactable
                password_input_field = wait.until(EC.presence_of_element_located((By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))

                # Clear any existing text (optional, but recommended)
                password_input_field.clear()

                # putting text in input field
                password_input_field.send_keys(X_PASSWORD)

                # next button click
                login_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')))
                login_button.click()

                #Writing post on X

                # Wait for the textbox input field to be clickable
                '''
                    current XPath is very long and can easily break if the site structure changes slightly.(which can make the element undetectable)
                    It’s better to find a shorter and more stable XPath or a CSS selector based on attributes
                '''
                text_box = wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]//div[@role="textbox"]')))

                # Click to focus
                text_box.click()

                # Use CTRL + A + DELETE instead of .clear()
                text_box.send_keys(Keys.CONTROL + "a")
                text_box.send_keys(Keys.DELETE)

                # Type your message
                text_box.send_keys(f"To my Internet Service Provider, why my internet speed is only {self.download}download/{self.upload}upload"
                                   f"when I pay for promise {PROMISED_DOWNLOAD}download/{PROMISED_UPLOAD}upload")

                #Hit Enter to post
                post_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')))
                post_button.click()
        except (ElementClickInterceptedException,TimeoutException):
            print("Time out or Couldn't find element! in x.com")






















