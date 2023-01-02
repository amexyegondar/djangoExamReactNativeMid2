from django.db import models
class empclass(models.Model):
       name=models.CharField(max_length=23)
       def __str__(self):
            return self.name
    
