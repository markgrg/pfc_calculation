from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=225)
