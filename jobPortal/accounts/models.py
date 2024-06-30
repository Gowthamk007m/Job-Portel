from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    COUNTRY_CHOICES = (
        ('IN', 'India'),
    )

    email = models.EmailField(
        'email address', unique=True, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(
        upload_to='user_photos/', blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    short_bio = models.TextField(max_length=500, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=1, default='M', choices=GENDER_CHOICES)
    country = models.CharField(
        max_length=50, default='IN', choices=COUNTRY_CHOICES)
    open_to_hiring = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def age(self):
        if self.dob:
            today = date.today()
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return None


class Address(models.Model):
    COUNTRY_CHOICES = (
        ('IN', 'India'),
    )
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    address_line_1 = models.TextField(max_length=250)
    address_line_2 = models.TextField(max_length=250)
    address_line_3 = models.TextField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(
        max_length=50, default='IN', choices=COUNTRY_CHOICES)
    pincode = models.CharField(max_length=25)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_default = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user', 'name']

    def __str__(self):
        return f'''{self.address_line_1}
        {self.address_line_2}
        {self.address_line_3}'''


class Hobby(models.Model):
    HOBBY_CHOICES = (
        ('Reading', 'Reading'),
        ('Traveling', 'Traveling'),
        ('Cooking', 'Cooking'),
        ('Sports', 'Sports'),
        ('Gardening', 'Gardening'),
        ('Gaming', 'Gaming'),
        ('Fitness', 'Fitness'),
        ('Photography', 'Photography'),
        ('Writing', 'Writing'),
        ('Dancing', 'Dancing'),
    )

    name = models.CharField(max_length=100, choices=HOBBY_CHOICES, unique=True)

    def __str__(self):
        return self.name


class UserHobby(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_hobbies', on_delete=models.CASCADE)
    hobbies = models.ManyToManyField(Hobby, related_name='user_hobbies')

    def __str__(self):
        return self.user.username

class Interest(models.Model):
    INTEREST_CHOICES = (
        ('Technology', 'Technology'),
        ('Science', 'Science'),
        ('Literature', 'Literature'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Health', 'Health'),
        ('Fitness', 'Fitness'),
        ('Education', 'Education'),
        ('Fashion', 'Fashion'),
        ('Entertainment', 'Entertainment'),
        ('Finance', 'Finance'),
        ('Politics', 'Politics'),
        ('Environment', 'Environment'),
        ('Sports', 'Sports'),
        ('History', 'History'),
    )
    
    name = models.CharField(max_length=100, choices=INTEREST_CHOICES, unique=True)

    def __str__(self):
        return self.name

        # class Interest(models.Model):
        #     INTEREST_CHOICES = (
        #         ('Technology', 'Technology'),
        #         ('Music', 'Music'),
        #         ('Art', 'Art'),
        #         ('Science', 'Science'),
        #     )

        #     name = models.CharField(max_length=100, choices=INTEREST_CHOICES, unique=True)

        #     def __str__(self):
        #         return self.name

        # class UserInterest(models.Model):
        #     user = models.ForeignKey(CustomUser, related_name='user_interests', on_delete=models.CASCADE)
        #     interest = models.ForeignKey(Interest, related_name='user_interests', on_delete=models.CASCADE)

        #     class Meta:
        #         unique_together = ('user', 'interest')

        #     def __str__(self):
        #         return f"{self.user.email} - {self.interest.name}"

        # class UserImage(models.Model):
        #     user = models.ForeignKey(CustomUser, related_name='images', on_delete=models.CASCADE)
        #     image = models.ImageField(upload_to='user_images/')

        #     def __str__(self):
        #         return self.image.url