from django.db import models

# Create your models here.
class Todo(models.Model):

    CHOICES = (
        ('M', 'Major'),
        ('N', 'Normal'),
        ('L', 'Later'),
    )

    title = models.CharField(max_length=120)
    description = models.TextField()
    priority = models.CharField(max_length=1, choices=CHOICES, default='N')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title + (self.priority)

