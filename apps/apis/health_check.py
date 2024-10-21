import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Check the health of the application'

    def handle(self, *args, **kwargs):
        url = 'https://tms.work.gd/api/health_check/'  # Replace with your actual URL
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.stdout.write(self.style.SUCCESS('Health check successful.'))
            else:
                self.stdout.write(self.style.ERROR('Health check failed. Status code: {}'.format(response.status_code)))
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR('Health check failed. Error: {}'.format(e)))
