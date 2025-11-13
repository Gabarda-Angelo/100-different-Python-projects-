import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib

# Load environment variables from .env file
load_dotenv()

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
'''
If you pass some headers along then Amazon's servers can give you the instant pot page in your language and also in your currency.
Also, it will make your request look (slightly) more human and less like a bot. Why? Headers include data that is sent over by a browser 
rather than a script. And many web servers like Amazon's may block requests they think originate from bots.
'''
header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
            "Dnt": "1",
            "Priority": "u=1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-Gpc": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
          }

def send_email_message(message, url):
    connection = smtplib.SMTP(os.environ["SMTP_EMAIL_PROVIDER_ADDRESS"], 587)
    my_email = os.environ["EMAIL_ADDRESS"]
    email_app_password = os.environ["EMAIL_APP_PASSWORD"]

    email_message_receiver = "angelogabarda.scc@gmail.com"
    with connection:
         connection.starttls()
         connection.login(my_email, email_app_password)
         # Send email BEFORE the connection closes
         status = connection.sendmail(
             from_addr=my_email,
             to_addrs=email_message_receiver,
             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
         )

    if status == {}:
        print("Email sent successfully")
    else:
        print("Email sent failed")


response = requests.get(URL,headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# First, try Amazon's standard price IDs , first check if Amazon gives us the full price in one single element (whole + decimal).
price_tag = soup.find("span", id="priceblock_ourprice") \
    or soup.find("span", id="priceblock_dealprice")

if price_tag:
    price = float(price_tag.get_text(strip=True).replace("$", "").replace(",", ""))

else:
    # Otherwise, get the whole + fraction separately
    whole = soup.find("span", class_="a-price-whole")
    fraction = soup.find("span", class_="a-price-fraction")
    if whole and fraction:
        # Remove commas and any extra dots from the whole part
        whole_clean = whole.get_text(strip=True).replace(",", "").replace(".", "")
        fraction_clean = fraction.get_text(strip=True)
        price_str = f"{whole_clean}.{fraction_clean}"
        price = float(price_str)
    else:
        price = None

# Final price check
if price is not None:
    print(f"Current Price: ${price:.2f}")

    # Set target price
    target_price = 100.00
    if price < target_price:
        message = f"Price dropped to ${price:.2f}!"
        send_email_message(message, URL)
else:
    print("Could not find the price. Amazon may be blocking the request.")
    with open("amazon_debug.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
    print("Check amazon_debug.html to inspect the returned HTML.")

