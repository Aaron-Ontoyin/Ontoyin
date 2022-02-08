from django.db import models


class Saying(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    

class Update(models.Model):
    topic = models.CharField(max_length=200)
    information = models.TextField()
    
    def __str__(self):
        return self.topic
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField()
    source = models.URLField(blank=True)
    source_email = models.EmailField(blank=True)  
    handle = models.CharField(max_length=200, blank=True)    
            
    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField()
    
    class Meta:
        verbose_name_plural = 'Galleries'
    
    def __str__(self):
        return self.name
    
    
class Upload(models.Model):
    title = models.CharField(max_length=200)
    info_pic = models.ImageField()
    info = models.TextField()
    url = models.URLField()
    
    def __str__(self):
        return self.title
