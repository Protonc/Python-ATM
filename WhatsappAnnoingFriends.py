from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group: ')
msg = input('Enter your message: ')
count = int(input('Enter the count: '))
gap = float(input('Interval (in seconds) between messages: '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) ').upper()

user = driver.find_element(By.XPATH, f'//span[@title="{name}"]')
user.click()

msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

for i in range(count):
    if bot_prompt == 'Y':
        msg_final = f"<Status: {i+1}/{count}> {msg}"
    else:
        msg_final = msg
    msg_box.send_keys(msg_final)
    send_button = driver.find_element(By.XPATH, '//button[@aria-label="Send"]')
    send_button.click()
    if gap > 0:
        time.sleep(gap)

msg_final = 'Bro just for fun now u will never ignore me dude'
msg_box.send_keys(msg_final)
send_button = driver.find_element(By.XPATH, '//button[@aria-label="Send"]')
send_button.click()

time.sleep(5)
driver.close()
