#  This might not be the best solution but it works
#  It tracks down first page of given site and returns if condition is right an email with link

import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.blocket.se/annonser/stockholm/elektronik/datorer_tv_spel/barbara_datorer?cg=5022&f=p&r=11'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


# def for sending email (gmail), two step verification
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your mail', 'password')
    subject = 'Great price'
    body = 'check the link!!! ' + url
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'sending mail',
        'reciving mail',
        msg
    )
    print('email has been sent!!!')
    server.quit()

# checking if there is macbook in adds
get_link = soup.find_all('a', class_='Link-sc-139ww1j-0 styled__StyledTitleLink-sc-1kpvi4z-10 enigRj')
for link in get_link:
    get_href = link.get('href')
    if '/macbook_' in get_href:
        #  if there is macbook go to that side and get price
        try:
            url = ('https://www.blocket.se' + get_href)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189"}
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
# making int of price and setting amount to check, if ok send mail def is activated
            price_raw = soup.find(
                class_='TextHeadline1__TextHeadline1Wrapper-sc-18mtyla-0 jwGyyY Price__StyledPrice-crp2x0-0 EkzGO')
            price1 = price_raw.string[0: -3]
            price2 = price1.split()
            price = int("".join(price2))
            if price <= 5000:
                send_email()
        except:
            print("Invalid price")
