from django.db import models
from django.db import models
from utils.models import CreatedUpdatedAt
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
#from django.core.validators import RegexValidator
from django.contrib.auth.base_user import BaseUserManager
import uuid
# Create your models here.



class UserManager(BaseUserManager):

    def create_user(self, email, username, password = None):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email id is required")
        user = self.model(email = email, username = username)
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_superuser(self, email, username, password = None):
        user = self.create_user(email, username, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self.db)
        return user
    

class UserModel(AbstractBaseUser, PermissionsMixin, CreatedUpdatedAt):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    #phone_number = models.CharField(unique=True, max_length=19, blank=False, validators=[phone_regex])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_image = models.ImageField(upload_to='user_image',null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    is_deleted = models.BooleanField(default=False)
    email = models.EmailField(unique=True, max_length=50)

    groups = models.ManyToManyField(Group, related_name='user_model_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_model_permissions', blank=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}, {self.username}"