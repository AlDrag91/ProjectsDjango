from django.db import models


# Create your models here.
class Datacont(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
