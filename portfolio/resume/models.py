# models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    path = models.CharField(max_length=255)  # Path to the image file
    github_url = models.URLField()  # URL to the GitHub repository

    def __str__(self):
        return self.title
