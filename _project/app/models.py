from django.db import models
from django.contrib.auth.hashers import make_password,check_password

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)

    def set_password(self, password):
        self.password_hash = make_password(password)

    def check_password(self, password):
        return check_password(password, self.password_hash)

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

class Destination(models.Model):
    name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_publicly = models.BooleanField(default=False)