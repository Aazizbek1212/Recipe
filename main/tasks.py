from django.core.mail import send_mail


def send_email():
    send_mail('test mail', 'test email',
    'azizbekilyosov1212@gmail.com', ['azizbekilyosov1212@gmail.com'], fail_silently=False)
    return 1