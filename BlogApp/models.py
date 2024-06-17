from django.db import models
from django.core.validators import validate_image_file_extension
# Create your models here.

class BlogPostModel(models.Model):
    blog_title=models.CharField(max_length=70)
    topic_title=models.CharField(max_length=80)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='image/',validators=[validate_image_file_extension])
    author=models.CharField(max_length=30)
    content=models.TextField()
