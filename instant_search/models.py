from django.db import models
from django.contrib import admin


class Student(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('name',) 
        
    def __unicode__(self):
        return self.name

    
admin.site.register(Student)
