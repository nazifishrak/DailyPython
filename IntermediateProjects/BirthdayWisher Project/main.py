import pandas
import datetime as dt
import random
import smtplib, ssl

username= 'nazifcodes@gmail.com'

# PASSWORD = input(f'Enter password for {username}: ')
PASSWORD = 'uysncohurevamycw'

bday_df = pandas.read_csv("./birthdays.csv")

today = dt.datetime.now()
today = (today.month, today.day)

bday_dict = {(data_row["month"], data_row["day"]): (
    data_row["name"], data_row['email']) for (index, data_row) in bday_df.iterrows()}


if today in bday_dict:
    random_letter = random.choice(['./letter_templates/letter_1.txt',
                                   './letter_templates/letter_2.txt',
                                   './letter_templates/letter_3.txt'])
    with open(random_letter, 'r') as letter:
        text = letter.read()
        text = text.replace("[NAME]", bday_dict[today][0])
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=username, password=PASSWORD)
        connection.sendmail(from_addr=username, to_addrs=bday_dict[today][1], msg=f"Subject: Happy Birthday\n\n{text}")