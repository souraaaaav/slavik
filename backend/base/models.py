from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
   
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=extra_fields['is_staff'],
                          is_active=extra_fields['is_active'],
                          is_superuser=extra_fields['is_superuser'],)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    is_personal_user = models.BooleanField(default=False)
    is_business_user = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    otp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.email
    
class ContactInfo(models.Model):
    full_name=models.CharField(max_length=30,blank=True,null=True)
    address=models.CharField(max_length=30,blank=True,null=True)
    city=models.CharField(max_length=30,blank=True,null=True)
    state=models.CharField(max_length=30,blank=True,null=True)
    zip=models.CharField(max_length=30,blank=True,null=True)
    phone=models.CharField(max_length=30,blank=True,null=True,unique=True)

    def __str__(self):
        return self.phone

class CompanyInfo(models.Model):
    CHOICE_OPTIONS = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    )
    company_name=models.CharField(max_length=30,blank=True,null=True)
    your_title=models.CharField(max_length=30,blank=True,null=True)
    business_started_in=models.CharField(max_length=30,blank=True,null=True)
    state=models.CharField(max_length=30,blank=True,null=True)
    crew_size=models.CharField(max_length=30,blank=True,null=True)
    category=models.CharField(max_length=30,blank=True,null=True,choices=CHOICE_OPTIONS)

    def __str__(self):
        return self.phone

class MetroArea(models.Model):
    CHOICE_OPTIONS = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    )
    location=models.CharField(max_length=30,null=True,blank=True,choices=CHOICE_OPTIONS)

    def __str__(self):
        return self.location

class PersonalUser(models.Model):
    user = models.OneToOneField(
        User, related_name="personal_user", on_delete=models.CASCADE)
    contact_info=models.OneToOneField(ContactInfo, related_name="personal_contact_info", on_delete=models.CASCADE,null=True,blank=True)
    metro_area=models.OneToOneField(MetroArea, related_name="personal_metro_area", on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.email

class BusinessUser(models.Model):
    user = models.OneToOneField(
        User, related_name="business_user", on_delete=models.CASCADE)
    contact_info=models.OneToOneField(ContactInfo, related_name="business_contact_info", on_delete=models.CASCADE,null=True,blank=True)
    metro_area=models.OneToOneField(MetroArea, related_name="business_metro_area", on_delete=models.CASCADE,null=True,blank=True)
    company_info=models.OneToOneField(CompanyInfo, related_name="business_company_info", on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.email
