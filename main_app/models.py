from django.db import models
from django.conf import settings
from login_reg_app.models import Client, Dev
from django.db.models import Q

class PostManager(models.Manager):
    def project_validator(self, postData):
        errors = {}
        if len(postData['proj_name']) < 2:
            errors['proj_name'] = 'Project Name must be longer than 2 characters'
        if len(postData['quick_pitch']) < 10:
            errors['quick_pitch'] = 'Pitch must be longer than 10 characters'
        if len(postData['desc']) < 10:
            errors['desc'] = 'Description must be longer than 10 characters'
        # if len(postData['category']) < 2:
        #     errors['category'] = 'Project Name must be longer than 2 characters'
        if int(postData['price']) < 1:
            errors['price'] = 'Price must be at least $1'


class Project(models.Model):
    name = models.CharField(max_length=20)
    pitch = models.CharField(max_length=40)
    about = models.CharField(max_length=500)
    category = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    times_viewed = models.IntegerField(default=0)
    creator = models.ForeignKey(Dev, related_name="developed_by", on_delete = models.CASCADE)
    watchers = models.ManyToManyField(Client, related_name="watched_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class Project_Image(models.Model):
    image = models.ImageField()
    project_pic = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    text = models.CharField(max_length=500)
    starter = models.ForeignKey(Client, related_name="started_by", on_delete = models.CASCADE)
    messager = models.ManyToManyField(Dev, related_name="messaged_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Reply(models.Model):
    post = models.CharField(max_length=255)
    dev_replier = models.ForeignKey(Dev, related_name="dev_replies", null = True, on_delete = models.CASCADE)
    client_replier = models.ForeignKey(Client, related_name="client_replies", null = True, on_delete = models.CASCADE)
    convo = models.ForeignKey(Chat, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

