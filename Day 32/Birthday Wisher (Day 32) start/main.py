# import smtplib
#
#
#
# my_email = "agabarda451@gmail.com" #The email here should have app password via google like in the instruction
# password = "zjkx unua ivup ejbz"  #app password provided by the email provider(gmail)
#
# '''
# This app is sending from gmail to yahoo account
# '''
#
# #using "with" keyword to close the connection
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()#transport layer security
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="gelo.gabarda@yahoo.com",
#         msg="Subject:Hello buboy\n\nThis is the body of my email."
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year = 1995,month=12,day=4 , hour=4)

print(date_of_birth)
