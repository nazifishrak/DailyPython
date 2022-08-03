import smtplib

MY_EMAIL = "nazif@ubcquantum.com"
password = 'Bangladesh123!'



























# Creating connection to mail provider by connecting to gmail server
with smtplib.SMTP('mail.ubcquantum.com') as connection:

    # Now we have to secure the connection we buillt so that our message is encrypted and intruders cannot intercept
    connection.starttls() #Secured our conmection

    connection.login(user=MY_EMAIL, password = password)

    connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                                msg="Subject:Hello\n\nTesting python SMTP module")