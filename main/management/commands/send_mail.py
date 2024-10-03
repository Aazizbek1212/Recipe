from django.core.management.base import BaseCommand
from main.tasks import send_email

class Command(BaseCommand):
    help = "Email jo'natish komandasi"

    def handle(self, *args, **kwargs):
        send_email()
        self.stdout.write(self.style.SUCCESS("Email muvaffaqiyatli jo'natildi!"))
