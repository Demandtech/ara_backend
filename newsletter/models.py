from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField()
