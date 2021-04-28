from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)
    #------------------------------
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked',blank=True)
    #------------------------------
    
    def __str__(self):
        return self.title
    #----------------------------------------------------------------
    """
    In this code we're gonna use the slugify() function provided by django
    to automatically generate the image slug for the given title when no slug is provided. 
    """
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    #-----------------------------------------------------------------
