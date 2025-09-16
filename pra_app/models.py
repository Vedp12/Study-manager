from django.db import models

# Create your models here.

class Password_manager(models.Model):
    App_pass = models.CharField(max_length=100)
    User_pass = models.CharField(max_length=100)
    email_pass = models.EmailField()
    password_pass  = models.CharField(max_length=100)
    
