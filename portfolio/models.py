from django.db import models

class Portfolio(models.Model):
    #home
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=100)

    #biography
    biography = models.TextField()

    #personal_info
    dob = models.DateField()
    gmail = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=50)

    #projects
    projects = models.TextField(max_length=200)

    def __str__(self):
        return (f"{self.name}")