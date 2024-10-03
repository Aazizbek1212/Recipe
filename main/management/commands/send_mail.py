from django.core.management.base import BaseCommand

from django.core.mail import send_mail


class Command(BaseCommand):
    help = "Email jo'natish komandasi"

    def handle(self, *args, **kwargs):
        send_mail('test mail', 'test email', 'azizbekilyosov1212@gmail.com',
                  ['azizbekilyosov1212@gmail.com'], fail_silently=False)
        self.stdout.write(self.style.SUCCESS("Email muvaffaqiyatli jo'natildi!"))
