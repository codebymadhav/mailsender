import smtplib

mymail="sender's mail address"

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=mymail,password=password)
connection.sendmail(from_addr=mymail,to_addrs="Receiver's mail address",msg="hello")
connection.close()
