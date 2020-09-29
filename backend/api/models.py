from django.db import models

# Create your models here.
class NewBug(models.Model):
    name = models.CharField('Name', max_length=240)
    email = models.EmailField()
    bugName = models.CharField("Bug", max_length=240)
    bugDescription = models.CharField("Description", max_length=1000)
    project = models.CharField("Project Description", max_length=240)
    date = models.DateField("Date", auto_now_add=True)
    
    def __str__(self):
        return self.name

class NewProject(models.Model):
    name = models.CharField('Name', max_length=240)
    email = models.EmailField()
    project_name = models.CharField('Project Name', max_length=240)
    project_desc = models.CharField("Project Description", max_length=240)
    date = models.DateField("Date", auto_now_add=True)

    def __str__(self):
        return self.project_name



