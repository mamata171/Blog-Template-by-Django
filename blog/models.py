from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name