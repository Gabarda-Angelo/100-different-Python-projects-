##################### Extra Hard Starting Project ######################
#Automize sending birthday wish thru gmail of the celebrant
import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

data_dict = data.to_dict(orient="records")

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
date_to_day = str(month)+"/"+str(day)+"/"+str(year)


# 2. Check if today matches a birthday in the birthdays.csv
for celebrant_info in data_dict:
    celebrant_birthmonth = celebrant_info["month"]
    celebrant_birthday = celebrant_info["day"]
    celebrant_birthyear = celebrant_info["year"]

    celebrant_email = celebrant_info["email"]
    celebrant_name = celebrant_info["name"]

    celebrant_birth_date = f"{celebrant_birthmonth}/{celebrant_birthday}/{celebrant_birthyear}"
    if date_to_day == celebrant_birth_date:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        chosen_letter_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{chosen_letter_number}.txt") as file:
            wish_letter = file.read()
            new_letter = wish_letter.replace("[NAME]", f"{celebrant_name}")
            my_wish_letter = new_letter

        # 4. Send the letter generated in step 3 to that person's email address.
        my_email = "agabarda451@gmail.com"
        password = "zjkx unua ivup ejbz"

        # using "with" keyword to close the connection
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()  # transport layer security
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=celebrant_email,
                msg=f"Subject:Happy Birthday Wish!\n\n{my_wish_letter}"
            )










