from optparse import Option
from tkinter import CASCADE
from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.forms import CharField
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from ckeditor.fields import RichTextField, CKEditorWidget

class Category(models.Model):

    Categories = (
        ('Deportes', 'Deportes'),
        ('Cine', 'Cine'),
        ('Música', 'Música'),
        ('Educación', 'Educación'),
        ('Politíca', 'Política'),
        ('Recetas', 'Recetas'),
        ('Tecnología','Tecnología'),
    )
    name = models.CharField(max_length=50, choices=Categories)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('', args=(str(self.id)))




class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status= 'published')
    option = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
   
    title = RichTextField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    subtitle = RichTextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', default=User)
    published = models.DateTimeField(default=timezone.now)
    image = models.ImageField()
    text = RichTextField()
    status = models.CharField(max_length=20, choices=option, default='draft')
    slug = models.SlugField(max_length=300, unique_for_date='published', null=False, unique=True)
    objects = models.Manager()
    postobjects = PostObjects()

    def get_absolute_url(self):
        return reverse('', args=(str(self.id)))

    class Meta:
        ordering = ('-published',)
        
        def __str__(self):
            return self.title


  
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null= True, blank = True)