
        text = text.replace("[NAME]", bday_dict[today][0])

        connection = smtplib.SMTP('mail.ubcquantum.com')
        connection.starttls()
        connection.login(user=username, password='Bangladesh123!')
        connection.sendmail(from_addr=username, to_addrs=bday_dict[today][1], msg=f"Subject: Happy Birthday\n\n{text}")