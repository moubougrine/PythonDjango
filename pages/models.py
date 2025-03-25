from django.db import models


class LoGing(models.Model):
    name=models.CharField(max_length=30 ,null=True)
    email=models.CharField(max_length=30 ,null=True)
    subject=models.TextField( null=True)
    text=models.TextField(null=True)
    def __str__(self):
        return self.subject
    