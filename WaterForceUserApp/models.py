from django.db import models

# Create your models here.

class ClientSlider(models.Model):
    image = models.FileField(upload_to='ClientSlider')
    name = models.CharField(max_length=1000)
    post  = models.CharField(max_length=1000)
    description = models.TextField()
    

class OurFeaturesSliderHome(models.Model):
    image = models.FileField(upload_to='OurFeaturesSliderHome')
    title = models.CharField(max_length=1000)
    description = models.TextField()

class AboutUsPageSlider(models.Model):
    image = models.FileField(upload_to='OurFeaturesSliderHome')
    title = models.CharField(max_length=1000)
    description = models.TextField()
    
class ServiceCategory(models.Model):
    title = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    
class Services(models.Model):
    Service_Category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField(upload_to='Services')
    title = models.CharField(max_length=1000)
    description = models.TextField()  
    
class Gallery(models.Model):
    title = models.CharField(max_length=1000)
    image = models.FileField(upload_to='Gallery')
    
class Contact(models.Model):
    fullname = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=50)
    message = models.TextField()
    