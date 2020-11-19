from django.db import models
import re
from django.db.models import Q
from django.conf import settings

# Create your models here.

# class PostQuerySet(models.QuerySet):
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query is not None:
#             or_lookup = (
#                 Q(fname__icontains=query) |
#                 Q(lname__icontains=query) |
#                 Q(alias__icontains=query) |
#                 Q(about__icontains=query)
#                 )
#             qs = qs.filter(or_lookup).distinct()
#             print(3)
#         return qs

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
    # def search(self, query=None):
    #     def get_queryset(self):
    #         print(4)
    #         return PostQuerySet(self.model, using=self._db)

    # def search(self, query=None):
    #     print(5)
    #     return self.get_queryset().search(query=query)

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