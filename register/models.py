from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default/default.png', upload_to='profile/')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image)


class Child(models.Model):
    parent = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='children')
    child_name = models.CharField(max_length=255, blank=True, null=True)
    child_age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(5), MaxValueValidator(13)])
    notes = models.CharField(max_length=2083, null=True, blank=True, default="")

    def __str__(self):
        return self.child_name
