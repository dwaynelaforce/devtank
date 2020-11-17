from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def registration_validator(self, postdata):
        errors = {}
        if len(postdata['fname']) < 2:
            errors['fname'] = "First name must be at least 2 characters"
        if len(postdata['lname']) < 2:
            errors['lname'] = "Last name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Invalid email address"
        if len(postdata['password']) < 8:
            errors['password'] = "Passwords must be at least 8 characters"
        if postdata['password'] != postdata['confirm_password']:
            errors['confirm_password'] = "Passwords do not match"
        return errors

class Client(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Dev(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    about = models.CharField(max_length=600, blank=True)
    profile_pic = models.ImageField(upload_to='media', default='media/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()