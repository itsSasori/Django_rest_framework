from django.db import models

# Create your models here.
class Advocate(models.Model):
    username = models.CharField(max_length=20)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.username
    
class Supreme(models.Model):
    advocate = models.ForeignKey(Advocate, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} - {self.advocate}"
