from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# from dotenv import load_dotenv
# from pathlib import Path

# env_path = Path('./environmentargs.env')
# load_dotenv(dotenv_path=env_path)


SENDER_EMAIL = os.environ['SENDER_EMAIL']
SENDER_PASSWORD = os.environ['SENDER_PASSWORD']
RECEIVER_EMAILS = os.environ['RECEIVER_EMAILS']
JOYCES_USERNAME = os.environ['JOYCES_USERNAME']
JOYCES_PASSWORD = os.environ['JOYCES_PASSWORD']

# SENDER_EMAIL = os.getenv('SENDER_EMAIL')
# SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')      
# RECEIVER_EMAILS = os.getenv('RECEIVER_EMAILS')
# JOYCES_USERNAME = os.getenv('JOYCES_USERNAME')
# JOYCES_PASSWORD = os.getenv('JOYCES_PASSWORD')

oldelements = []
#

def email():
    print("sending email")

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = SENDER_EMAIL
    receiver_email = RECEIVER_EMAILS.split(',')  # Enter receiver address
    password = SENDER_PASSWORD
    
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


def main(oldelements):
    print("Searching...")
    origlen = len(oldelements)
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("window-size=1920,1080")

    chromedriver = "./chromedriver"
    driver = webdriver.Chrome(service = Service(chromedriver), options=chrome_options)
    # chromedriver = ChromeDriverManager().install()

    # driver = webdriver.Chrome(chromedriver)

    url = 'https://www.tds.ms/CentralizeSP/Student/Login/joycesdrivingschool'
    driver.get(url)

    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    username.send_keys(JOYCES_USERNAME)

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys(JOYCES_PASSWORD)

    sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/form[1]/div[6]/button')
    sign_in.click()

    driver.get('https://www.tds.ms/CentralizeSP/BtwScheduling/Lessons?SchedulingTypeId=1')

    tbody2 = driver.find_element(By.XPATH, '//*[@id="datepicker"]/div/div[2]/table/tbody')
    elements2 = tbody2.find_elements(By.CLASS_NAME, 'ui-state-available')

    tbody = driver.find_element(By.XPATH, '//*[@id="datepicker"]/div/div[1]/table/tbody')
    elements = tbody.find_elements(By.CLASS_NAME, 'ui-state-available')

    oldelements = elements + elements2

    newlen = len(oldelements)

    print("found", len(elements) + len(elements2))
    driver.quit()
    if (len(elements) > 0 or len(elements2) > 0) and newlen != origlen:
        email()

    return oldelements

print("Starting program...")


while (True):
    oldelements = main(oldelements = oldelements)
    time.sleep(300)



