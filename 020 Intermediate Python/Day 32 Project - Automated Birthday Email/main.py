
import smtplib
import datetime as dt
import random
import pandas

now=dt.datetime.now()
month=now.month
day=now.day
content = ""
name=""
to_email=""
my_email=EMAIL
my_pw=PASSWORD
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        #make connection secure
        connection.starttls()
        connection.login(user=my_email,password=my_pw)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                        msg=f"Subject: Happy Birthday!\n\n {content}")
def get_body():
    num=random.randint(1,3)
    global content
    with open(f"./letter_templates/letter_{num}.txt") as letter:
        content=letter.read()
    print(content)

list=pandas.read_csv("birthdays.csv")
name_list=list.to_dict(orient="records")

print(name_list)
for i in name_list:

    if i["month"]==month and i["day"]==day:
        name=i["name"]
        to_email=i["email"]
        get_body()
        content=content.replace("[NAME]",name)
        print(content)
        send_email()













