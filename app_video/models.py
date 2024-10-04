from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Video(models.Model):
    # Title of the video (cannot be blank)
    title = models.CharField(max_length=200, blank=False)

    # Choices for category
    CATEGORY_CHOICES = [
        ('EDU', 'Education'),
        ('ENT', 'Entertainment'),
        ('TECH', 'Technology'),
        ('LIFE', 'Lifestyle'),
        ('SPORT', 'Sports'),
        ('MUSIC', 'Music'),
        ('NEWS', 'News'),
    ]
    # Category of the video (cannot be blank)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, blank=False)

    # URL to the video (cannot be blank)
    link = models.URLField(max_length=250, blank=False)

    # Thumbnail URL (cannot be blank)
    thumbnail = models.URLField(max_length=250, blank=False)

    # String representation
    def __str__(self):
        return self.title
  

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    commented_video=models.ForeignKey(Video,on_delete=models.CASCADE)
    comment_text=models.TextField(max_length=500,blank=False)
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_text or "No Comment"

