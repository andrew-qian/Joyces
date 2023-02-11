from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from pathlib import Path

# dotenv_path = Path('./environmentargs.env')
# load_dotenv(dotenv_path=dotenv_path)

# SENDER_EMAIL = os.getenv('EMAIL')
# SENDER_PASSWORD = os.getenv('PASSWORD')
# RECEIVER_EMAILS = os.getenv('EMAILS')


def email():
    print("sending email")

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = SENDER_EMAIL
    print("Sender email:", sender_email)  # Enter your address
    receiver_email = RECEIVER_EMAILS.split(',')  # Enter receiver address
    print("receiver emails: ", receiver_email)
    password = SENDER_PASSWORD
    print("Password: ", password)
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Joyce's BTW Available"

    text = """\
    will implement date, time, instructor later"""

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        for i in range(len(receiver_email)):
            server.sendmail(sender_email, receiver_email[i], message.as_string())


def main():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = "./chromedriver.exe"
    driver = webdriver.Chrome(service = Service(chromedriver), options=chrome_options)
    # chromedriver = ChromeDriverManager().install()

    # driver = webdriver.Chrome(chromedriver)
    driver.minimize_window()

    url = 'https://www.tds.ms/CentralizeSP/Student/Login/joycesdrivingschool'
    driver.get(url)

    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    username.send_keys('Qia12779')

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys('9418123')

    sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/form[1]/div[6]/button')
    sign_in.click()

    driver.get('https://www.tds.ms/CentralizeSP/BtwScheduling/Lessons?SchedulingTypeId=1')

    table = driver.find_element(By.CLASS_NAME, 'ui-datepicker-calendar')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    elements = tbody.find_elements(By.CLASS_NAME, 'ui-state-unavailable')

    print("found", len(elements))
    driver.quit()
    if len(elements) > 0:
        email()

print("Starting program...")
print("Env vars:", SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAILS)

while (True):
    main()
    time.sleep(300)



