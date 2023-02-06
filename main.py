from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def email():
    print("sending email")

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "joycesbot@gmail.com"  # Enter your address
    receiver_email = ["andrewyukaiqian@gmail.com", "gradtolentino@icloud.com", "kr4chdown@gmail.com"]  # Enter receiver address
    password = "ditkurjeflpsginm"
    
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
    chromedriver = "./chromedriver"
    driver = webdriver.Chrome(service = Service(chromedriver))
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
    elements = tbody.find_elements(By.CLASS_NAME, 'ui-state-available')

    print("found", len(elements))
    driver.quit()
    if len(elements) > 0:
        email()
print("Starting program...")
while (True):
    main()
    time.sleep(1200)



