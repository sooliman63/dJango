from django.db import models

# Create your models here.
class Movies_Info(models.Model):
    name = models.CharField(max_length=100,help_text="The Neme Of The Movie.")
    date = models.DateField(verbose_name="Date The Movie Was Released.")