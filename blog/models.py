from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.db.models.signals import post_save,post_delete
import funcoes
from bs4 import BeautifulSoup

class Menu(models.Model):
    name = models.CharField(max_length=80)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Internal")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    resume = models.CharField(max_length=200, unique=False,default='')
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    detach = models.BooleanField(default=False)
    sidebar = models.BooleanField(default=False)
    footer=models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=False,default='')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class File(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=False,default='')
    file = models.FileField(upload_to='images')

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


def Comment_save(signal, instance, sender, **kwargs):

    post=''.join(BeautifulSoup(Post.objects.get(title=instance.post).content, "html.parser").stripped_strings)

    if funcoes.similarity(instance.body,post) > 0.0 :
        instance.active=True
    else:
        instance.active=False



    


signals.pre_save.connect(Comment_save, sender=Comment)

