import streamlit as st
import requests
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from dotenv import load_dotenv
import random
from random import randint

host_ip_address = os.getenv("HOST_IP_ADDRESS")

# Load environment variables from the .env file
load_dotenv()

st.title("User Registration")

my_email = os.getenv('MY_EMAIL')
password = os.getenv('APP_PASSWORD')

# User registration
def registration():
    username = st.text_input("Username", key="reg_username")
    full_name = st.text_input("Full Name", key="full_name")
    email = st.text_input("Email", key="email")
    password = st.text_input("Password", type="password", key="reg_password")

    if st.button("Register"):
        if not username or not full_name or not email or not password:
            st.error("All fields are required.")
        else:
            response = requests.post(
                f"http://{host_ip_address}:8000/register",
                json={"username": username, "full_name": full_name, "email": email, "password": password},
            )
            if response.status_code == 200:
                st.success("Registration successful. You can now log in.")
                send_registration_email(email, username)
            else:
                st.error("Registration failed. Username may already be taken.")


def send_registration_email(user_email, username):
    my_quotes = [line.strip() for line in open('pages/quotes.txt')]
    quote = random.choice(my_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        message = f"Hello {username},\n\n"
        message += "Nice to have you here!\n\n"
        message += "Please feel free to send your feedback to this email. We're constantly working on making user experience the best.\n\n"
        message += f"We believe in positive impact so, a motivational quote before you leave:\n{quote}"
         # Create a message container
        msg = MIMEMultipart()
        msg['Subject'] = "A welcome note from developers"
        msg['From'] = my_email
        msg['To'] = user_email
   
        msg.attach(MIMEText(message, 'plain'))

        # Attach the image (change the image path)
        with open('pages/image.jpg', 'rb') as image_file:
            image = MIMEImage(image_file.read(), _subtype='jpg')
            image.add_header('Content-Disposition', 'attachment', filename='your-image.jpg')
            msg.attach(image)

        connection.sendmail(from_addr=my_email, to_addrs=user_email, msg=msg.as_string())

if __name__ == "__main__":
    registration()
    