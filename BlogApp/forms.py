from django import forms
from .models import BlogPostModel

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPostModel
        fields=['blog_title','topic_title','image','author','content']