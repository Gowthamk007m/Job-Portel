# accounts/models.py
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'password']
    

    objects = UserManager()

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    work_status = models.CharField(max_length=50, choices=[('F', 'Fresher'), ('E', 'Experienced')])
    phone_number = models.CharField(max_length=15, blank=True)
    contact_email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    languages = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    years_of_exp = models.CharField(max_length=2)

class Certification(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='certifications')
    certification_name = models.TextField()
    expiration_date = models.DateField()

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='educations')
    level_of_education = models.CharField(max_length=100, choices=[
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
        ('Diploma', 'Diploma'),
        ('Certification', 'Certification')
    ])
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.level_of_education} in {self.course_name}"

class Experience(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"