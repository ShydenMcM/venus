from django.db import models

# Create your models here.


class Landing(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=300)

    def __str__(self):
        """this function showing me summary on the admin panel"""
        return self.summary
