from django.conf import settings
from django.core.mail import send_mail

def email_send(subject,msg,email):
    subject=subject
    msg=msg
    from_email = settings.EMAIL_HOST_USER
    email_list = [email]
    send_mail(subject,msg,from_email,email_list)