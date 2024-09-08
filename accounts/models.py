from django.db import models
from django.contrib.auth.models import User

THEME_CHOICES = {
    "dark": "dark",
    "light": "light"

}

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    theme = models.CharField(max_length=5, choices=THEME_CHOICES, default="dark")