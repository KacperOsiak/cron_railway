from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
class Joke(models.Model):
    joke_id = models.IntegerField(unique=True)  
    setup = models.CharField(max_length=255)
    punchline = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.setup} -> {self.punchline}"