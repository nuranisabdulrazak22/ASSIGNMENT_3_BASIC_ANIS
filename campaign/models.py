from django.db import models

class Volunteer(models.Model):
    INTEREST_CHOICES = [
        ('tree_planting', 'Tree Planting'),
        ('beach_cleanup', 'Beach Cleanup'),
        ('awareness_talk', 'Climate Awareness Talks'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    interest = models.CharField(max_length=50, choices=INTEREST_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
