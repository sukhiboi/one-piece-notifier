import os
import requests
import smtplib

from bs4 import BeautifulSoup
from email.message import EmailMessage

MANGA_URL = os.environ.get("MANGA_URL")
CHAPTER_NUMBER = os.environ.get("CHAPTER_NUMBER")

NOTIFICATION_FROM_EMAIL = os.environ.get("NOTIFICATION_FROM_EMAIL")
NOTIFICATION_TO_EMAIL = os.environ.get("NOTIFICATION_TO_EMAIL")

SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

def check_chapter_available(chapter_number):
    url = f"{MANGA_URL}-{chapter_number}/"
    response = requests.get(url)
    html = BeautifulSoup(response.text, features="html.parser")
    result = html.find('h1', {'itemprop': "headline"})
    headline = result.text
    return headline.__contains__(" – ")

def notify_about_new_chapter(chapter_number):
    msg = EmailMessage()

    msg.set_content(f"{MANGA_URL}-{chapter_number}/")
    msg['Subject'] = f'One Piece chapter {chapter_number} is available'
    msg['From'] = NOTIFICATION_FROM_EMAIL
    msg['To'] = NOTIFICATION_TO_EMAIL

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    s.send_message(msg)
    s.quit()

def main():
    chapter_number = CHAPTER_NUMBER
    is_available = check_chapter_available(chapter_number)
    if is_available:
        notify_about_new_chapter(chapter_number)

if __name__ == "__main__":
    main()