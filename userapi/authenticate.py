import string, secrets, os, smtplib
from email.message import EmailMessage
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from rest_framework.response import Response

def authenticate_invoice():
    pass

def authenticate_return():
    pass

def verification_email(source_email, to_email, password, verification_link):
        msg = EmailMessage()
        msg['Subject'] = 'Verify Your Account'
        msg['From'] = source_email
        msg['To'] = to_email

        msg.set_content('Please verify your account by clicking the link: ' + verification_link)

        html_content = f"""
        <html>
        <body>
            <h1>Welcome to OneReturn!</h1>
            <p>Please click the button below to verify your account:</p>
            <a href="{verification_link}" style="background-color: #007BFF; color: white; padding: 14px 25px; text-align: center; text-decoration: none; display: inline-block;">Verify Account</a>
            <p> If you did not sign up for this service you can ignore and delete this email</p>
        </body>
        </html>
        """

        msg.add_alternative(html_content, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
             server.login(source_email, password)
             server.send_message(msg)