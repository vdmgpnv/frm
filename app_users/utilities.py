from django.template.loader import render_to_string
from django.core.signing import Signer
from django.core.mail import send_mail

from forum.settings import ALLOWED_HOSTS, EMAIL_HOST_USER

signer = Signer()

def send_activation_notofocation(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user' : user, 'host' : host, 'sign' : signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/activation_letter_body.txt', context)
    send_mail(
    subject,
    body_text,
    EMAIL_HOST_USER,
    [user.email],
    fail_silently=False,
)