import pandas
import datetime as dt
import random
import smtplib

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
def read_birthdates():
    now = dt.datetime.now()
    data = pandas.read_csv("birthdays.csv")
    all_data = data.to_dict(orient="records")
    for row in all_data:
        name = row["name"]
        email = row["email"]
        year = row["year"]
        month = row["month"]
        day = row["day"]
        match_found = check_day(year, month, day)
        if match_found:
            print("Ready to send email")
            letter_template = select_letter_template()
            greeting_letter_contents = read_letter_template(letter_template, name)
            send_letter(name=name, message_to_send=greeting_letter_contents)


def check_day(year, month, day):
    today = dt.datetime.today().strftime('%-m-%-d')
    birth_day = f"{month}-{day}"
    if today == birth_day:
        return True
    else:
        return False


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def select_letter_template():
    letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    selected_letter = random.choice(letter_list)
    return selected_letter


def read_letter_template(letter_template, name):
    path_to_file = f"letter_templates/{letter_template}"
    with open(path_to_file, "r") as file:
        file_data = file.read()
        new_data = file_data.replace('[NAME]', name)
        return new_data


# 4. Send the letter generated in step 3 to that person's email address.
def send_letter(name, message_to_send):
    my_email = "rendheer_joshy@yahoo.com"
    password = "toxjwadamcckymbh"
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jrendheer@gmail.com",
            msg=f"Subject:Happy Happy Birthday {name}\n\n{message_to_send}"
        )

read_birthdates()