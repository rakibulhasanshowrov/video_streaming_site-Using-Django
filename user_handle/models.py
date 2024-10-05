from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
  dob=models.DateField(blank=True,null=True)
  profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
  type=[
    ('Genaral_user','General User'),
    ('Teacher','Teacher'),
    ('Student','Student'),  
  ]
  profile_type=models.CharField(max_length=30,blank=False,choices=type,default="General User")
  
  
  def __str__(self):
    return self.user.username
  
