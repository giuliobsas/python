from django.db import models

class cliente(models.Model): 
    
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    
