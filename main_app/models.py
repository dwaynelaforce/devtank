from django.db import models
from login_reg_app.models import Client, Dev

class Project(models.Model):
    name = models.CharField(max_length=20)
    pitch = models.CharField(max_length=40)
    about = models.CharField(max_length=500)
    category = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    creator = models.ForeignKey(Dev, related_name="developed_by", on_delete = models.CASCADE)
    watchers = models.ManyToManyField(Client, related_name="watched_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project_Image(models.Model):
    image = models.ImageField(upload_to='media/project_pics')
    project_pic = models.ForeignKey(Project, related_name="project_pics", on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

# class Chat(models.Model):
#     text = models.CharField(max_length=500)
#     starter = models.ForeignKey(Client, related_name="started_by", on_delete = models.CASCADE)
#     messager = models.ManyToManyField(Dev, related_name="messaged_by")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
# class Reply(models.Model):
#     post = models.CharField(max_length=255)
#     replier = models.ForeignKey(User, related_name="replies", null = True, on_delete = models.CASCADE)
#     convo = models.ForeignKey(Chat, related_name="comments", on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Project_Messages(models.Model):
#     post = models.CharField(max_length=300)
#     project = models.ForeignKey(Project, related_name='project_comments', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
