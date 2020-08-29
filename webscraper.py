import requests
from bs4 import BeautifulSoup
import smtplib
url="https://www.nike.com/in/u/custom-kyrie-6-by-you-10000753/1577691261047"
headers={
    "User-Agent":"Search google and paste the user agent here"
}
def check_price():
    page=requests.get(url,headers)
    soup=BeautifulSoup(page.content,'html.parser')
    c=soup.find(id='navWrapper').get_text()
    price=soup.find(class_="product-price css-11s12ax is--current-price").get_text()
    converted_price=price[2:8]
    print(converted_price)
    send_email()
    


    # if float(converted_price) < 1000:
    #     send_email()

 
def send_email():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(' enter your sending email','password')
    subject="Price fell down "
    body="check the link broo https://www.nike.com/in/u/custom-kyrie-6-by-you-10000753/1577691261047"
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail('sending email','Sender Email ',msg)
    print('Email sent!!!')
    server.quit()

# check_price()
check_price()