from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=D:\Documents\chrome_data")  # Path to browser session
chrome_options.add_argument("--profile-directory=Default")   #default profile


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com')


print("If you're not logged in, scan the QR code to log in to WhatsApp Web.")
input("Press Enter to continue...")



def click_unread_button():
    try:
        unread_button = driver.find_element(By.XPATH, '//button[@aria-pressed="false" and @data-tab="4"]//div[text()="Unread"]')
        unread_button.click()
        print("Unread button clicked.")
    except Exception as e:
        print(f"Error clicking unread button: {e}")
def find_unread_chats():
    try:
        unread_chats = driver.find_elements(By.XPATH, '//span[@aria-label="Unread messages"]')
        print(f"Found {len(unread_chats)} unread chats.")
        return unread_chats
    except Exception as e:
        print(f"Error in finding unread chats: {e}")
        return []


def read_last_message():
    try:
        messages = driver.find_elements(By.XPATH, '//div[contains(@class,"message-in")]')
        if messages:
            return messages[-1].text
    except Exception as e:
        print(f"Error reading the last message: {e}")
    return ""


def send_reply(reply_text):
    try:
        input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        input_box.send_keys(reply_text)
        input_box.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Error sending reply: {e}")


try:
    click_unread_button()
    while True:
        unread_chats = find_unread_chats()

        if unread_chats:
            for chat in unread_chats:

                chat.click()
                time.sleep(2)


                last_message = read_last_message()
                print(f"New message: {last_message}")


                if "hello" in last_message.lower():
                    send_reply("Hi there! How can I assist you?")
                elif "help" in last_message.lower():
                    send_reply("Sure, let me know your issue.")
                else:
                    send_reply("I am here to help you!")

        time.sleep(5)
except KeyboardInterrupt:
    print("Stopping the automation...")
finally:
    driver.quit()
