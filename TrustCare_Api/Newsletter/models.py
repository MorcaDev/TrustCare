from django.db import models

# STORED EMAILS
class NewsLetterEmail(models.Model):

    id = models.AutoField(primary_key=True,blank=False, null=False, unique=True) 
    email = models.EmailField(max_length=45, unique=True) 

    def __str__(self):
        return self.email

# POSTS 
class Post(models.Model):

    id = models.AutoField(primary_key=True,blank=False, null=False, unique=True) 
    title = models.CharField(max_length=45, blank=False, null=False)
    content_text = models.TextField(blank=False, null=False)
    content_media = models.FileField(upload_to='posts/',blank=False, null=False) 

    def __str__(self):
        return self.title