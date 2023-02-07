from django.db import models
from users.manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

letters = RegexValidator(r'^[a-zA-Z. ]*$', 'Only letters are allowed.')


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """ Overrides Django Base User. """

    #username = None
    email = models.EmailField(max_length=500, unique=True)
    first_name = models.CharField(max_length=80, null=True, blank=True, validators=[letters])
    last_name = models.CharField(max_length=80, null=True, blank=True, validators=[letters])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='profile_images', default='defaultAvatar.png')
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return "{}".format(self.email)