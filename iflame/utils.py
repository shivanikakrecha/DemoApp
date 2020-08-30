from django.core.mail import send_mail
from django.conf import settings


def send_email_to_user(subject=None, message_body=None, from_user=None, to_user=None):
    from_user = settings.EMAIL_HOST_USER
    send_mail(subject, message_body, from_user, to_user)
    return
