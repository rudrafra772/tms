from django.db import models


class ColorChoices(models.TextChoices):
    blue = 'blue', 'blue'
    yellow = 'yellow', 'yellow'
    purple = 'purple', 'purple'
    green = 'green', 'green'
    red = 'red', 'red'