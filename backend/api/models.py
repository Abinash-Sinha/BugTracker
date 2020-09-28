from django.db import models

# Create your models here.
class NewBug(models.Model):
    name = model.CharField('Name', max_length=240)
    email = model.EmailField()
    bugName = model.CharField("Bug")
    bugDescription = model.CharField("Description")
    project = model.CharField("Project Description")
    date = model.DateField("Date", auto_now_add=True)
    
    def __str__(self):
        return self.name
    