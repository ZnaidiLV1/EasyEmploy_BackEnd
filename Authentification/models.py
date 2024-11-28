from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser, Group, \
    Permission
from django.db import models
from django.utils.crypto import get_random_string

from Address.models import Address


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    verification_code = models.CharField(max_length=6, default='100000', editable=True)
    user_image = models.ImageField(upload_to="images/", blank=True, null=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    # Client Fields
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    age_user = models.PositiveIntegerField(null=True, blank=True)
    num_tlfn = models.IntegerField(max_length=20, null=True, blank=True)  # Phone numbers as strings
    # Entreprise Fields
    name = models.CharField(max_length=100, null=True, blank=True)
    ref_entreprise = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = get_random_string(8)  # Generate a random username
        super().save(*args, **kwargs)

    objects = CustomUserManager()

