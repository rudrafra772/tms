from django.core.management.base import BaseCommand
from apps.auth.models import UserModel
from faker import Faker

class Command(BaseCommand):
    help = 'Create fake users'

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, default=1000, help='Number of fake users to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        users = []
        password = 'password123'
        chunk_size = 100  # You can adjust this value as needed
        import random
        for i in range(total):
            email = fake.unique.email()
            username = fake.unique.user_name()
            is_active = True
            is_staff = random.choice([True, False])
            is_superuser = random.choice([True, False]) if is_staff else False
            user = UserModel(
                email=email,
                username=username,
                is_active=is_active,
                is_staff=is_staff,
                is_superuser=is_superuser
            )
            user.set_password(password)
            users.append(user)
            if len(users) >= chunk_size:
                UserModel.objects.bulk_create(users)
                users = []
        if users:
            UserModel.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} fake users.'))