from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length = 20)
    author = models.CharField(max_length = 20)
    content = models.TextField()
    create_time = models.DateField(auto_now_add = True)
    update_time = models.DateField(auto_now = True)

