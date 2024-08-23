from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(null = True, blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE) #deletes all users meals if user is deleted

    #created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("meal-detail", kwargs={"pk": self.pk}) #redirect to home


  

    def __str__(self):
        return self.title
