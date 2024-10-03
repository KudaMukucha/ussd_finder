from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Code(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_codes')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,unique=True)
    code = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_codes')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-created']
        indexes = [
            models.Index(fields=['created'])
        ]

        def __str__(self):
            return self.name
