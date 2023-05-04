from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser account with a specified username."

    def add_arguments(self, parser):
        parser.add_argument(
            "username",
            nargs="?",
            default="admin",
            help='Optional username for the superuser. Default value is "admin".',
        )
        parser.add_argument(
            "password",
            nargs="?",
            default="admin",
            help='Optional password for the superuser. Default value is "admin".',
        )

    def handle(self, *args, **options):
        USER = get_user_model()

        username = options["username"]
        password = options["password"]

        USER.objects.create_superuser(username=username, email="admin@example.com", password=password)

        self.stdout.write(
            self.style.SUCCESS(f"Superuser created successfully.😊 \nusername: {username} \nPassword: {password}")
        )
