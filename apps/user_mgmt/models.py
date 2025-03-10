from django.db import models
from utils.models import BaseModel
from apps.auth.models import UserModel
from datetime import datetime, timezone
from utils.helper.date_and_time import current_time, datetime_in_timezone, formatted_time
from django.utils.timezone import timedelta
import pytz

# Create your models here.
class Attendance(BaseModel, models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    in_time = models.DateTimeField(null=True, blank=True)
    out_time = models.DateTimeField(null=True, blank=True)

    def duration(self):
        if self.in_time and self.out_time:
            return self.out_time - self.in_time
        elif self.in_time:
            output = datetime_in_timezone(datetime.now()) - datetime_in_timezone(self.in_time)
            return formatted_time(output)
        else:
            return None
    
    def __str__(self):
        return f"{self.user.username} - {self.in_time} - {self.out_time}"
